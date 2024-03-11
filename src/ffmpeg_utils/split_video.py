import subprocess
from pathlib import Path
from typing import Annotated

import typer


def split_video(
    input: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ],
    prefix: bool = False,
    offset: int = 0,
) -> None:
    duration = get_duration(input)
    split(input, duration, prefix, offset)


def get_duration(video: Path) -> int:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(video.resolve()),
        ],
        capture_output=True,
    ).stdout.decode("utf-8")
    seconds = float(result)
    return round(seconds / 3600)


def split(video: Path, number: int, keep_prefix: bool = False, offset: int = 0) -> None:
    video_name = video.stem
    video_ext = video.suffix
    for i in range(number):
        start = str(i).zfill(2)
        if i == number - 1:
            end = str(i + 2).zfill(2)
        else:
            end = str(i + 1).zfill(2)
        if keep_prefix:
            filename = f"{video_name}_{str(i + 1 + offset).zfill(2)}{video_ext}"
        else:
            filename = f"{str(i + 1 + offset).zfill(2)}{video_ext}"

        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-i",
                str(video.resolve()),
                "-ss",
                f"{start}:00:00",
                "-to",
                f"{end}:00:00",
                "-c",
                "copy",
                filename,
            ]
        )


def main() -> None:
    typer.run(split_video)
