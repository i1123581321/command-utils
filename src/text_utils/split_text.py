import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="text-split",
    description="split text file by line no",
)

parser.add_argument("filename", type=str, help="input file path")
parser.add_argument("lineno", nargs="+", type=int, help="line numbers")


def main():
    args = parser.parse_args()
    filename = Path(args.filename)
    lineno: list[int] = args.lineno
    lineno = list(map(lambda x: x - 1, lineno))
    lineno.sort()
    result: list[str] = []
    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()
        start = 0
        for i in lineno:
            result.append("".join(content[start:i]))
            start = i
        result.append("".join(content[start:]))
    name, ext = filename.stem, filename.suffix
    for i, r in enumerate(result):
        Path(f"{name}-{i + 1:02}{ext}").write_text(r, encoding="utf-8")
