#!/usr/bin/env python3
import os
import subprocess
import sys

URL = os.getenv("YOUTUBE_URL")
if not URL:
    sys.exit("❌  YOUTUBE_URL missing")

COOKIES = "youtube.com_cookies.txt"

subprocess.run(
    ["yt-dlp", "--cookies", COOKIES, "-f", "bv*+ba/b", "--no-part", "-o", "video.mp4", URL.strip()],
    check=True,
)

subprocess.run(
    ["yt-dlp", "--cookies", COOKIES, "-x", "--audio-format", "mp3", "--no-part", "-o", "audio.mp3", URL.strip()],
    check=True,
)

print("✅  video.mp4  and  audio.mp3  ready")
