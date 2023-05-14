import subprocess
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser(
    prog="clip-video", description="clip video by start timestamp and duration"
)

parser.add_argument("input", type=Path, help="video to be cliped")
parser.add_argument("start", type=str, help="start timestamp")
parser.add_argument("duration", type=str, help="clip duration")


def main() -> None:
    args = parser.parse_args()
    filename: Path = args.input
    if not filename.exists():
        print(f"{filename.resolve()} dose not exist")
        exit(-1)

    output = f"clip{filename.suffix}"

    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-ss",
            args.start,
            "-i",
            str(filename.resolve()),
            "-to",
            args.duration,
            "-c",
            "copy",
            output,
        ]
    )
