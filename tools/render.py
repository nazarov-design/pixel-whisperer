#!/usr/bin/env python3
"""Render sample-design HTML files to PNG with headless Chrome.

Usage: python3 tools/render.py FILE.html [FILE.html ...]
Each HTML declares its canvas: <meta name="render-size" content="1000x1400">.
Output: FILE.png next to the HTML.
"""
import os
import re
import shutil
import subprocess
import sys

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "", shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
]


def chrome():
    for c in CHROME_CANDIDATES:
        if c and os.path.exists(c):
            return c
    sys.exit("Chrome/Chromium not found.")


def render(path):
    html = open(path, encoding="utf-8").read()
    m = re.search(r'name="render-size" content="(\d+)x(\d+)"', html)
    w, h = (m.group(1), m.group(2)) if m else ("1000", "1400")
    out = os.path.splitext(path)[0] + ".png"
    subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={w},{h}",
                    f"--screenshot={os.path.abspath(out)}", "file://" + os.path.abspath(path)],
                   check=True, capture_output=True)
    print(out)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        render(p)
