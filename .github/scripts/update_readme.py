#!/usr/bin/env python3
"""
=============================================================================
 Refresh the live YouTube block inside README.md
=============================================================================
 Runs inside the "Update README (YouTube live)" GitHub Action, but it works
 locally too:   python .github/scripts/update_readme.py

 It rewrites ONLY the text between these markers in README.md:

   <!-- YT-SUBS:START -->  ... <!-- YT-SUBS:END -->    subscriber count
   <!-- YT-VIDEO:START --> ... <!-- YT-VIDEO:END -->   3 compact video rows

 If a fetch fails, that block is left exactly as it was, so the README can
 never end up broken or empty.

 The rows are laid out like the video list beside a YouTube video: a small
 thumbnail on the LEFT, the title on the RIGHT, and the whole thing is a
 link (no "Watch on YouTube" button needed).

 Data sources, in order of preference:
   1. YouTube Data API v3   - exact numbers, used when YT_API_KEY is set
                              (repo secret). Costs ~9 of the 10,000 free
                              quota units per run.
   2. YouTube channel page  - subscriber count, no key needed
   3. YouTube RSS feed      - newest video, no key needed
=============================================================================
"""

import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

CHANNEL_ID = "UC-Oc7NNVa0oW3nHI1L-3oKQ"
UPLOADS_ID = "UU" + CHANNEL_ID[2:]  # the channel's "uploads" playlist
HANDLE = "Rom_Flasher"
CHANNEL_URL = f"https://www.youtube.com/@{HANDLE}"
API = "https://www.googleapis.com/youtube/v3"

README = "README.md"

SUBS_START = "<!-- YT-SUBS:START -->"
SUBS_END = "<!-- YT-SUBS:END -->"
VIDEO_START = "<!-- YT-VIDEO:START -->"
VIDEO_END = "<!-- YT-VIDEO:END -->"

# How many of the newest uploads we are willing to look at when hunting for
# the all-time most watched / most liked video.
SCAN_LIMIT = 200

# On-screen width of the small thumbnail in the list.
THUMB_WIDTH = 150

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
#  YouTube Data API v3  (needs YT_API_KEY)
# ---------------------------------------------------------------------------
def api_key():
    return os.environ.get("YT_API_KEY", "").strip()


def api(path, **params):
    """Call the API. Never lets the key leak into an error message."""
    key = api_key()
    if not key:
        raise RuntimeError("YT_API_KEY is not set")

    params["key"] = key
    url = f"{API}/{path}?" + urllib.parse.urlencode(params)
    try:
        raw = get(url)
    except urllib.error.HTTPError as ex:
        body = ex.read().decode("utf-8", "replace")[:200]
        raise RuntimeError(f"HTTP {ex.code}: {body}") from None
    except Exception as ex:  # noqa: BLE001 - message must stay key-free
        raise RuntimeError(type(ex).__name__) from None

    data = json.loads(raw)
    if "error" in data:
        raise RuntimeError(data["error"].get("message", "unknown API error"))
    return data


def api_channel():
    """Exact subscriber / video / view totals for the channel."""
    data = api("channels", part="statistics", id=CHANNEL_ID)
    stats = data["items"][0]["statistics"]
    out = {
        "subs": int(stats.get("subscriberCount", 0) or 0),
        "videos": int(stats.get("videoCount", 0) or 0),
        "views": int(stats.get("viewCount", 0) or 0),
    }
    log("[OK]", f"api channel: {out['subs']} subs, {out['videos']} videos")
    return out


def thumb_url(thumbs):
    """Prefer 'medium' - it is 320x180 (true 16:9, no black bars) and always
    exists, so it stays crisp at THUMB_WIDTH without loading a 1280x720 file."""
    for name in ("medium", "maxres", "high", "default"):
        url = (thumbs.get(name) or {}).get("url")
        if url:
            return url
    return ""


def api_videos():
    """Every upload with its exact view / like counts."""
    ids = []
    token = ""
    while len(ids) < SCAN_LIMIT:
        params = {
            "part": "contentDetails",
            "maxResults": 50,
            "playlistId": UPLOADS_ID,
        }
        if token:
            params["pageToken"] = token
        page = api("playlistItems", **params)
        ids += [i["contentDetails"]["videoId"] for i in page.get("items", [])]
        token = page.get("nextPageToken", "")
        if not token:
            break

    out = []
    for start in range(0, len(ids), 50):
        page = api(
            "videos",
            part="statistics,snippet",
            id=",".join(ids[start : start + 50]),
        )
        for item in page.get("items", []):
            snippet = item.get("snippet", {})
            stats = item.get("statistics", {})
            out.append(
                {
                    "id": item["id"],
                    "title": html.unescape(snippet.get("title", "")).strip(),
                    "published": snippet.get("publishedAt", ""),
                    "views": int(stats.get("viewCount", 0) or 0),
                    "likes": int(stats.get("likeCount", 0) or 0),
                    "thumb": thumb_url(snippet.get("thumbnails", {})),
                }
            )
    log("[OK]", f"api videos: {len(out)}")
    return out


# ---------------------------------------------------------------------------
#  fallbacks that need no API key
# ---------------------------------------------------------------------------
def scrape_subscribers():
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


def rss_videos():
    xml = get(f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}")
    out = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        vid = re.search(r"<yt:videoId>([^<]+)</yt:videoId>", entry)
        title = re.search(r"<title>(.*?)</title>", entry, re.S)
        if not (vid and title):
            continue
        published = re.search(r"<published>([^<]+)</published>", entry)
        out.append(
            {
                "id": vid.group(1),
                "title": html.unescape(title.group(1)).strip(),
                "published": published.group(1) if published else "",
                "views": 0,
                "likes": 0,
                # mqdefault is always present and is 16:9 (320x180).
                "thumb": f"https://i.ytimg.com/vi/{vid.group(1)}/mqdefault.jpg",
            }
        )
    log("[OK]", f"rss videos: {len(out)}")
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
#  picking the three rows
# ---------------------------------------------------------------------------
def pick_rows(videos):
    """Newest, most watched and most liked - always three DIFFERENT videos.

    The all-time most watched video is very often also the most liked one, in
    which case showing it twice would look silly. When that happens we take the
    next one down and say "fan favourite" instead of claiming the #1 spot.
    """
    if not videos:
        return []

    rows = []
    used = set()

    def take(video, label):
        rows.append((video, label))
        used.add(video["id"])

    newest = max(videos, key=lambda v: v.get("published", ""))
    take(newest, f"🔥 LATEST&nbsp;&nbsp;·&nbsp;&nbsp;📅 {pretty_date(newest.get('published', ''))}")

    for key, top_label, alt_label in (
        ("views", "🏆 MOST WATCHED", "🔥 POPULAR VIDEO"),
        ("likes", "❤️ MOST LIKED", "❤️ FAN FAVOURITE"),
    ):
        ranked = sorted(videos, key=lambda v: v[key], reverse=True)
        best = next((v for v in ranked if v["id"] not in used and v[key] > 0), None)
        if not best:
            continue
        label = top_label if ranked[0]["id"] == best["id"] else alt_label
        take(best, f"{label}&nbsp;&nbsp;·&nbsp;&nbsp;{best[key]:,} {key}")

    return rows


def video_row(video, label):
    """Thumbnail floats left, the title sits next to it, everything links."""
    url = f"https://www.youtube.com/watch?v={video['id']}"
    title = html.escape(video["title"])
    thumb = video.get("thumb") or f"https://i.ytimg.com/vi/{video['id']}/mqdefault.jpg"

    return "\n".join(
        [
            f'<a href="{url}"><img src="{thumb}" width="{THUMB_WIDTH}" '
            f'align="left" alt="{title}"/></a>',
            f'<a href="{url}"><b>{title}</b></a><br/>',
            f"<sub>{label}</sub>",
            '<br clear="all"/>',
        ]
    )


def video_block(rows):
    # No blank lines anywhere: this has to stay ONE raw HTML block, otherwise
    # GitHub starts wrapping pieces in <p> and the float layout falls apart.
    if not rows:
        return None
    return "\n<br/>\n".join(video_row(video, label) for video, label in rows)


# ---------------------------------------------------------------------------
#  markdown builders
# ---------------------------------------------------------------------------
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

    subs = None
    videos = []

    if api_key():
        try:
            subs = human_count(api_channel()["subs"])
        except Exception as ex:
            log("[WARN]", f"api channel failed ({ex}); falling back to the page")
        try:
            videos = api_videos()
        except Exception as ex:
            log("[WARN]", f"api videos failed ({ex}); falling back to rss")
    else:
        log("[i]", "no YT_API_KEY - using the page / rss fallbacks")

    if not videos:
        try:
            videos = rss_videos()
        except Exception as ex:
            log("[WARN]", f"rss failed: {ex}")

    if not subs:
        try:
            subs = scrape_subscribers()
        except Exception as ex:
            log("[WARN]", f"subscriber lookup failed: {ex}")

    changed = False

    text, c = replace_block(text, SUBS_START, SUBS_END, subs_block(subs))
    changed |= c

    text, c = replace_block(text, VIDEO_START, VIDEO_END, video_block(pick_rows(videos)))
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
