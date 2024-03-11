import subprocess
from pathlib import Path
from typing import Annotated

import typer

from ffmpeg_utils.common import time_validator


def clip_video(
    input: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ],
    start: Annotated[str, typer.Argument(callback=time_validator)],
    duration: Annotated[str, typer.Argument(callback=time_validator)],
) -> None:
    output = f"clip{input.suffix}"

    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-ss",
            start,
            "-i",
            str(input.resolve()),
            "-to",
            duration,
            "-c",
            "copy",
            output,
        ]
    )


def main() -> None:
    typer.run(clip_video)
