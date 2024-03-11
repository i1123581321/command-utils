import subprocess
from pathlib import Path

import typer


def zip_all() -> None:
    for f in Path.cwd().iterdir():
        if f.is_dir():
            subprocess.run(["7z", "a", "-tzip", f"{f.name}.zip", f"./{f.name}/*"])


def main() -> None:
    typer.run(zip_all)
