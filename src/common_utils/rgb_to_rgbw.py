import re
from typing import Annotated

import typer


def hex_callback(value: str) -> str:
    if re.match(r"^[0-9a-fA-F]{6}$", value) is not None:
        return value
    raise typer.BadParameter("please input valid hex color code")


def trim(i: int) -> int:
    if i < 0:
        return 0
    if i > 255:
        return 255
    return i


def rgb_to_rgbw(hex: Annotated[str, typer.Argument(callback=hex_callback)]) -> None:
    r = int(hex[0:2], base=16)
    g = int(hex[2:4], base=16)
    b = int(hex[4:6], base=16)

    m = max(r, g, b)
    output = [0, 0, 0, 0]
    if m != 0:
        multiplier = 255.0 / m
        hr = r * multiplier
        hg = g * multiplier
        hb = b * multiplier

        luminance = (
            ((max(hr, hg, hb) + min(hr, hg, hb)) / 2.0 - 127.5)
            * (255 / 127.5)
            / multiplier
        )

        output[0] = int(r - luminance)
        output[1] = int(g - luminance)
        output[2] = int(b - luminance)
        output[3] = int(luminance)

    print(",".join([str(trim(x)) for x in output]))


def main() -> None:
    typer.run(rgb_to_rgbw)
