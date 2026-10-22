"""
Weekly release helper for the Rom Flasher tool.

Run this every week. It bumps the version, records what changed, and tells you
exactly what to run next. Nothing here touches the network or git history - it
only edits two files and prints a checklist.

    python _weekly_release.py --note "Fixed OTG detection on Redmi Note 13"

The two files it keeps in step:

    app/build.gradle.kts        versionCode 4 -> 5, versionName 1.2.0 -> 1.2.1
    app/src/main/.../MainActivity.kt   APP_VERSION "1.2.0" -> "1.2.1"

Keeping APP_VERSION in MainActivity equal to versionName is what makes the
in-app update check work: the app compares its own version against the newest
GitHub release tag.
"""

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GRADLE = ROOT / "app" / "build.gradle.kts"
ACTIVITY = ROOT / "app" / "src" / "main" / "java" / "com" / "romflasher" / "tool" / "MainActivity.kt"
CHANGELOG = ROOT / "CHANGELOG.md"


def read(path):
    if not path.exists():
        sys.exit("missing file: %s" % path)
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8")


def bump_version_name(name):
    """1.2.0 -> 1.2.1, 1.2 -> 1.2.1, 1.2.9 -> 1.3.0 (patch only, by design)."""
    parts = [int(x) for x in re.findall(r"\d+", name)]
    while len(parts) < 3:
        parts.append(0)
    parts[2] += 1
    return ".".join(str(x) for x in parts[:3])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", required=True,
                    help="one short line about what changed, shown in the app")
    ap.add_argument("--dry-run", action="store_true", help="show the plan, change nothing")
    args = ap.parse_args()

    gradle = read(GRADLE)
    activity = read(ACTIVITY)

    m_code = re.search(r"versionCode\s*=\s*(\d+)", gradle)
    m_name = re.search(r'versionName\s*=\s*"([^"]+)"', gradle)
    if not m_code or not m_name:
        sys.exit("could not find versionCode / versionName in app/build.gradle.kts")

    old_code = int(m_code.group(1))
    old_name = m_name.group(1)
    new_code = old_code + 1
    new_name = bump_version_name(old_name)

    print("Rom Flasher weekly release")
    print("-" * 52)
    print("  versionCode : %d  ->  %d" % (old_code, new_code))
    print("  versionName : %s  ->  %s" % (old_name, new_name))
    print("  note        : %s" % args.note)
    print()

    if args.dry_run:
        print("dry run - nothing written")
        return

    gradle = re.sub(r"versionCode\s*=\s*\d+", "versionCode = %d" % new_code, gradle, count=1)
    gradle = re.sub(r'versionName\s*=\s*"[^"]+"', 'versionName = "%s"' % new_name, gradle, count=1)
    write(GRADLE, gradle)

    if not re.search(r'APP_VERSION\s*=\s*"[^"]+"', activity):
        sys.exit("could not find APP_VERSION in MainActivity.kt")
    activity = re.sub(r'APP_VERSION\s*=\s*"[^"]+"',
                      'APP_VERSION = "%s"' % new_name, activity, count=1)
    write(ACTIVITY, activity)

    today = datetime.date.today().isoformat()
    entry = "\n## v%s - %s\n\n- %s\n" % (new_name, today, args.note)
    if CHANGELOG.exists():
        write(CHANGELOG, read(CHANGELOG).rstrip() + "\n" + entry)
    else:
        write(CHANGELOG, "# Rom Flasher changes\n" + entry)

    print("  app/build.gradle.kts   updated")
    print("  MainActivity.kt        updated")
    print("  CHANGELOG.md           updated")
    print()
    print("Next:")
    print("  1. make one small real change to the app (see --note above)")
    print("  2. build the APKs")
    print("  3. gh release create v%s --title \"ROM Flasher Tool v%s\" --notes \"%s\""
          % (new_name, new_name, args.note))
    print("  4. the app on users' phones will offer the update on its next quiet moment")


if __name__ == "__main__":
    main()
