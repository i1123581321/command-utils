from pathlib import Path
from sys import stdin
from typing import Optional

import typer


def convert_quote(
    filename: Optional[Path] = typer.Argument(default=None), encoding: str = "utf-8"
) -> None:
    if filename is not None:
        content = filename.read_text(encoding=encoding)
    else:
        content = "\n".join([line for line in stdin])

    content = (
        content.replace("\u201c", "\u300c")
        .replace("\u201d", "\u300d")
        .replace("\u2018", "\u300e")
        .replace("\u2019", "\u300f")
    )

    if filename is not None:
        filename.write_text(content, encoding="utf-8")
    else:
        print(content)


def main() -> None:
    typer.run(convert_quote)
