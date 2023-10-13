import subprocess
from pathlib import Path
from typing import Annotated

import typer

from ffmpeg_utils.common import time_validator


def video_to_gif(
    filename: Annotated[
        Path,
        typer.Argument(
            exists=True, dir_okay=False, resolve_path=True, help="video name"
        ),
    ],
    start: Annotated[
        str,
        typer.Argument(
            callback=time_validator,
            help="start time, format: [HOURS:]MM:SS[.MILLISECONDS]",
        ),
    ],
    end: Annotated[
        str,
        typer.Argument(
            callback=time_validator,
            help="end time, format: [HOURS:]MM:SS[.MILLISECONDS]",
        ),
    ],
    fps: Annotated[int, typer.Option(help="gif fps")] = 24,
    height: Annotated[int, typer.Option(help="gif max height")] = 400,
    max_color: Annotated[int, typer.Option(help="gif max color num")] = 256,
    output: Annotated[Path, typer.Option(help="generated gif filename")] = Path(
        "output.gif"
    ),
) -> None:
    """Use ffmpeg to convert video to gif based on start and end timestamps"""

    fps_str = f"fps={fps}"
    scale_str = f"scale=-1:{height}:flags=lanczos"
    palette_gen = f"palettegen=max_colors={max_color}:stats_mode=diff"
    palette_use = "paletteuse=dither=bayer:bayer_scale=3:diff_mode=rectangle"
    split_str = f"split[s0][s1];[s0]{palette_gen}[p];[s1][p]{palette_use}"

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-ss",
            start,
            "-to",
            end,
            "-copyts",
            "-i",
            filename,
            "-vf",
            f"{fps_str},{scale_str},{split_str}",
            "-loop",
            "0",
            output,
        ]
    )
    subprocess.run(["gifsicle", "-b", "-O3", output])


def main() -> None:
    typer.run(video_to_gif)
