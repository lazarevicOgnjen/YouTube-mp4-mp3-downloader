#!/usr/bin/env python3
import os
import subprocess
import sys

URL = os.getenv("YOUTUBE_URL")
if not URL:
    sys.exit("❌  YOUTUBE_URL missing")

COOKIES = os.getenv("YOUTUBE_COOKIES")
if not COOKIES:
    sys.exit("❌  YOUTUBE_COOKIES secret missing")

with open("cookies.txt", "w") as f:
    f.write(COOKIES)

subprocess.run(
    ["yt-dlp", "--cookies", "cookies.txt", "-f", "bv*+ba/b", "--no-part", "-o", "video.mp4", URL.strip()],
    check=True,
)

subprocess.run(
    ["yt-dlp", "--cookies", "cookies.txt", "-x", "--audio-format", "mp3", "--no-part", "-o", "audio.mp3", URL.strip()],
    check=True,
)

print("✅  video.mp4  and  audio.mp3  ready")
