from pathlib import Path
from typing import Annotated

import pikepdf
import typer


def unlock_pdf(
    filename: Annotated[
        Path, typer.Argument(exists=True, dir_okay=False, resolve_path=True)
    ],
    password: str,
    remove_origin: bool = False,
) -> None:
    origin = filename.parent / f"{filename.stem}.origin.pdf"
    Path.rename(filename, origin)
    pdf = pikepdf.open(origin, password=password)
    pdf.save(filename)
    pdf.close()
    if remove_origin:
        Path.unlink(origin)


def main() -> None:
    typer.run(unlock_pdf)


if __name__ == "__main__":
    main()
