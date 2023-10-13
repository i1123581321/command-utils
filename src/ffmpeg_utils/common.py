import re

import typer

time_pattern = r"^(?:\d+:)?[0-5][0-9]:[0-5][0-9](?:\.\d+)?$"


def time_validator(time: str) -> str:
    if re.match(time_pattern, time):
        return time
    else:
        raise typer.BadParameter("timestamp format: [HH:]MM:SS[.m...]")
