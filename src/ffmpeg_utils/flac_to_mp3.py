import subprocess
from pathlib import Path

import typer


def flac_to_mp3() -> None:
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


def main() -> None:
    typer.run(flac_to_mp3)
