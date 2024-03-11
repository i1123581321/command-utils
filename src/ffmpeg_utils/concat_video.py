import subprocess
from pathlib import Path
from typing import Annotated

import typer


def concat_video(
    videos: Annotated[
        list[Path], typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ],
    output: Annotated[Path, typer.Option(dir_okay=False, resolve_path=True)] = Path(
        "output.mkv"
    ),
) -> None:
    Path("list.txt").write_text("\n".join(f"file '{x}'" for x in videos))
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            "list.txt",
            "-c",
            "copy",
            str(output),
        ]
    )
    Path("list.txt").unlink()


def main() -> None:
    typer.run(concat_video)
