import subprocess
from pathlib import Path

import typer


def extract_audio(video_ext: str = "mp4", audio_ext: str = "m4a") -> None:
    for file in Path.cwd().iterdir():
        if file.name.endswith(video_ext):
            subprocess.run(
                [
                    "ffmpeg",
                    "-v",
                    "error",
                    "-i",
                    file.name,
                    "-vn",
                    "-acodec",
                    "copy",
                    f"{file.stem}.{audio_ext}",
                ]
            )


def main() -> None:
    typer.run(extract_audio)
