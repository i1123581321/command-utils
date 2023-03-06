import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="zip-all", description="zip all subfolder into individual zip archives"
)


def main():
    _ = parser.parse_args()
    for f in Path.cwd().iterdir():
        if f.is_dir():
            subprocess.run(["7z", "a", "-tzip", f"{f.name}.zip", f"./{f.name}/*"])
