from pathlib import Path
from typing import Annotated

import typer


def split_text(
    filename: Annotated[
        Path,
        typer.Argument(exists=True, dir_okay=False, resolve_path=True),
    ],
    lineno: list[int] = typer.Argument(default=None),
) -> None:
    lines = filename.read_text(encoding="utf-8").split("\n")
    if len(lineno) == 0:
        lineno = [i for i, line in enumerate(lines) if line.startswith("# ")]
        lineno.remove(0)
    else:
        lineno = list(map(lambda x: x - 1, sorted(lineno)))
    result: list[str] = []
    start = 0
    for i in lineno:
        result.append("\n".join(lines[start:i]))
        start = i
    result.append("\n".join(lines[start:]))
    for i, r in enumerate(result):
        Path(f"{filename.stem}-{i + 1:0>2}{filename.suffix}").write_text(
            r, encoding="utf-8"
        )


def main() -> None:
    typer.run(split_text)
