import subprocess
from pathlib import Path

import typer


def delay_sub(pattern: str, time: str, output: Path = Path("output")) -> None:
    if not output.exists():
        output.mkdir()

    for f in Path().cwd().glob(pattern):
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-itsoffset",
                time,
                "-i",
                str(f.resolve()),
                "-c",
                "copy",
                str((output / f.name).resolve()),
            ]
        )


def main() -> None:
    typer.run(delay_sub)
