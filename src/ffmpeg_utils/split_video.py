import argparse
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(prog="split_video",
                                 description="Divide the video into paragraphs of about 1 hour")

parser.add_argument("input",
                    type=str,
                    help="Video path to be split")

parser.add_argument("-p",
                    "--prefix",
                    type=bool,
                    default=False,
                    help="keep video name as output prefix")


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
            str(video.resolve())
        ],
        capture_output=True).stdout.decode("utf-8")
    seconds = float(result)
    return round(seconds / 3600)


def split(video: Path, number: int, keep_prefix: bool = False):
    video_name = video.stem
    video_ext = video.suffix
    for i in range(number):
        start = str(i).zfill(2)
        if i == number - 1:
            end = str(i + 2).zfill(2)
        else:
            end = str(i + 1).zfill(2)
        if keep_prefix:
            filename = f"{video_name}_{str(i + 1).zfill(2)}{video_ext}"
        else:
            filename = f"{str(i + 1).zfill(2)}{video_ext}"

        subprocess.run([
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
            filename
        ])


def main():
    args = parser.parse_args()
    video = Path(args.input)
    if not video.exists():
        print(f"file not exist: {args.input}", file=sys.stderr)
        sys.exit(-1)
    duration = get_duration(video)
    split(video, duration, args.prefix)
