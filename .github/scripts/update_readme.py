#!/usr/bin/env python3
"""
=============================================================================
 Refresh the live YouTube block inside README.md
=============================================================================
 Runs inside the "Update README (YouTube live)" GitHub Action, but it works
 locally too:   python .github/scripts/update_readme.py

 It rewrites ONLY the text between these markers in README.md:

   <!-- YT-SUBS:START -->  ... <!-- YT-SUBS:END -->    subscriber count
   <!-- YT-VIDEO:START --> ... <!-- YT-VIDEO:END -->   latest video card

 If a fetch fails, that block is left exactly as it was, so the README can
 never end up broken or empty.

 Data sources (in order):
   1. YouTube Data API v3  - used only when the YT_API_KEY secret is set
   2. YouTube channel page - plain HTTPS, no key, always available
   3. YouTube RSS feed     - latest videos, no key, very reliable
=============================================================================
"""

import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime

CHANNEL_ID = "UC-Oc7NNVa0oW3nHI1L-3oKQ"
HANDLE = "Rom_Flasher"
CHANNEL_URL = f"https://www.youtube.com/@{HANDLE}"
README = "README.md"

SUBS_START = "<!-- YT-SUBS:START -->"
SUBS_END = "<!-- YT-SUBS:END -->"
VIDEO_START = "<!-- YT-VIDEO:START -->"
VIDEO_END = "<!-- YT-VIDEO:END -->"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def log(level, msg):
    print(f"{level} {msg}", flush=True)


def get(url, timeout=30):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept-Language": "en-US,en;q=0.9",
            # Skips YouTube's EU cookie/consent interstitial.
            "Cookie": "CONSENT=YES+cb.20210328-17-p0.en+FX+700",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def human_count(n):
    """2030 -> 2.03K, 1500000 -> 1.50M (same style YouTube shows)."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.2f}M"
    if n >= 1_000:
        return f"{n / 1_000:.2f}K"
    return str(n)


# ---------------------------------------------------------------------------
#  subscriber count
# ---------------------------------------------------------------------------
def subscribers():
    # 1) official API, only if a key was provided as a repo secret
    key = os.environ.get("YT_API_KEY", "").strip()
    if key:
        try:
            raw = get(
                "https://www.googleapis.com/youtube/v3/channels"
                f"?part=statistics&id={CHANNEL_ID}&key={urllib.parse.quote(key)}"
            )
            data = json.loads(raw)
            count = int(data["items"][0]["statistics"]["subscriberCount"])
            log("[OK]", f"subscribers via API: {count}")
            return human_count(count)
        except Exception as ex:
            log("[WARN]", f"API lookup failed ({ex}); falling back to the page")

    # 2) scrape the public channel page
    for url in (CHANNEL_URL, f"https://www.youtube.com/channel/{CHANNEL_ID}"):
        try:
            page = get(url)
            m = re.search(r"([\d.,]+[KMB]?)\s+subscribers", page)
            if m:
                log("[OK]", f"subscribers via page: {m.group(1)}")
                return m.group(1)
            log("[WARN]", f"no subscriber text found on {url}")
        except Exception as ex:
            log("[WARN]", f"scrape failed for {url}: {ex}")

    return None


# ---------------------------------------------------------------------------
#  latest video (RSS)
# ---------------------------------------------------------------------------
def latest_videos():
    xml = get(f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}")
    out = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        vid = re.search(r"<yt:videoId>([^<]+)</yt:videoId>", entry)
        title = re.search(r"<title>(.*?)</title>", entry, re.S)
        if not (vid and title):
            continue
        published = re.search(r"<published>([^<]+)</published>", entry)
        views = re.search(r'<media:statistics views="(\d+)"', entry)
        out.append(
            {
                "id": vid.group(1),
                "title": html.unescape(title.group(1)).strip(),
                "published": published.group(1) if published else "",
                "views": views.group(1) if views else "",
            }
        )
    log("[OK]", f"rss videos found: {len(out)}")
    return out


def pretty_date(iso):
    if not iso:
        return ""
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return f"{dt.day} {dt.strftime('%b %Y')}"
    except Exception:
        return ""


# ---------------------------------------------------------------------------
#  markdown builders
# ---------------------------------------------------------------------------
def md_text(s):
    """Escape the characters that would break a markdown link label."""
    for ch in ("\\", "[", "]", "*", "_", "`"):
        s = s.replace(ch, "\\" + ch)
    return s


def subs_block(subs):
    if not subs:
        return None
    value = urllib.parse.quote(subs, safe="")
    return (
        "[![YouTube Subscribers]"
        f"(https://img.shields.io/badge/YouTube%20Subscribers-{value}-FF0000"
        "?logo=youtube&logoColor=white)]"
        f"({CHANNEL_URL})"
    )


def video_block(video):
    if not video:
        return None
    url = f"https://www.youtube.com/watch?v={video['id']}"
    alt = html.escape(video["title"], quote=True)

    meta = []
    date = pretty_date(video["published"])
    if date:
        meta.append(f"Uploaded {date}")
    if video["views"]:
        meta.append(f"{int(video['views']):,} views")
    meta.append(f"[Watch on YouTube]({url})")

    return "\n".join(
        [
            '<div align="center">',
            "",
            f'<a href="{url}">',
            f'  <img src="https://i.ytimg.com/vi/{video["id"]}/hqdefault.jpg" '
            f'width="480" alt="{alt}"/>',
            "</a>",
            "",
            f"**[{md_text(video['title'])}]({url})**",
            "",
            "*" + " · ".join(meta) + "*",
            "",
            "</div>",
        ]
    )


# ---------------------------------------------------------------------------
#  README surgery
# ---------------------------------------------------------------------------
def replace_block(text, start, end, new_content):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        log("[ERROR]", f"markers not found in README: {start}")
        return text, False
    if new_content is None:
        log("[i]", f"kept existing block ({start})")
        return text, False
    replacement = f"{start}\n{new_content}\n{end}"
    updated = pattern.sub(lambda _m: replacement, text, count=1)
    return updated, updated != text


def main():
    if not os.path.exists(README):
        log("[ERROR]", f"{README} not found")
        return 1

    with open(README, encoding="utf-8") as fh:
        text = fh.read()

    try:
        videos = latest_videos()
    except Exception as ex:
        videos = []
        log("[WARN]", f"rss failed: {ex}")

    try:
        subs = subscribers()
    except Exception as ex:
        subs = None
        log("[WARN]", f"subscriber lookup failed: {ex}")

    changed = False

    text, c = replace_block(text, SUBS_START, SUBS_END, subs_block(subs))
    changed |= c

    text, c = replace_block(
        text, VIDEO_START, VIDEO_END, video_block(videos[0] if videos else None)
    )
    changed |= c

    if changed:
        with open(README, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        log("[OK]", "README.md refreshed")
    else:
        log("[OK]", "nothing to change")

    return 0


if __name__ == "__main__":
    sys.exit(main())
