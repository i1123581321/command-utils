from pathlib import Path

import typer


def rename_sub(
    video_ext: str = "mkv", sub_ext: str = "ass", suffix_num: int = -1
) -> None:
    videos = [p for p in Path.cwd().iterdir() if p.suffix == f".{video_ext}"]
    subtitles = [p for p in Path.cwd().iterdir() if p.suffix == f".{sub_ext}"]
    if len(subtitles) % len(videos) != 0:
        print(f"warning {len(subtitles)} is not an integer multiple of {len(videos)}")
        return
    n = len(subtitles) // len(videos)
    i = 0
    rename_files: list[tuple[str, str]] = []
    for video in videos:
        j = 0
        while j < n:
            name_before = subtitles[i].name
            suffixes = subtitles[i].suffixes
            if suffix_num == -1:
                suffix_num = len(suffixes)
            suffix_num = min(len(suffixes), suffix_num)
            suffixes = suffixes[len(suffixes) - suffix_num :]
            name_after = f"{video.stem}{''.join(suffixes)}"
            print(f"{name_before} -> {name_after}")
            j += 1
            i += 1
            rename_files.append((name_before, name_after))
    flag = typer.prompt("rename?", type=bool)
    if flag:
        for before, after in rename_files:
            Path(before).rename(after)


def main() -> None:
    typer.run(rename_sub)
