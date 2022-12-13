import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="flac-to-mp3",
    description="convert flac file to mp3 file in current directory",
)


def main():
    _ = parser.parse_args()
    for f in Path.cwd().glob("*.flac"):
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-i",
                str(f.resolve()),
                "-ab",
                "320k",
                f"{f.stem}.mp3",
            ]
        )
