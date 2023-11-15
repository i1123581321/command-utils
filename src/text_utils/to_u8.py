from pathlib import Path

import typer
from charset_normalizer import from_bytes


def convert(path: Path) -> None:
    raw_content = path.read_bytes()
    Path(f"{path.name}.bak").write_bytes(raw_content)
    result = from_bytes(raw_content)
    if (best := result.best()) is not None:
        content = raw_content.decode(encoding=best.encoding)
        content = content.replace("\r\n", "\n")
        path.write_text(content, encoding="utf-8")


def to_u8(suffix: str) -> None:
    for file in Path.cwd().iterdir():
        if file.is_file() and file.name.endswith(suffix):
            convert(file)


def main() -> None:
    typer.run(to_u8)
