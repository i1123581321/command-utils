from html import unescape
from pathlib import Path
from typing import Annotated

import typer


def mdify(
    filename: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ],
    encoding: str = "utf-8",
) -> None:
    # 分割文件
    lines = filename.read_text(encoding=encoding).split("\n")
    # 去除空行
    lines = [line.strip() for line in lines if line.strip() != ""]
    # 转换 html 实体
    lines = list(map(lambda x: unescape(x), lines))

    Path(f"{filename.stem}.md").write_text("\n\n".join(lines), encoding="utf-8")


def main() -> None:
    typer.run(mdify)
