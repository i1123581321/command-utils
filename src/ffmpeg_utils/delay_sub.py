import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="delay-sub", description="call ffmpeg to delay sub files"
)

parser.add_argument("filename", type=str)
parser.add_argument("time", type=str)
parser.add_argument("-o", "--output", type=Path, default=(Path.cwd() / "output"))


def main() -> None:
    args = parser.parse_args()
    output: Path = args.output

    if not output.exists():
        output.mkdir()

    for f in Path().cwd().glob(args.filename):
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-itsoffset",
                args.time,
                "-i",
                str(f.resolve()),
                "-c",
                "copy",
                str((output / f.name).resolve()),
            ]
        )
