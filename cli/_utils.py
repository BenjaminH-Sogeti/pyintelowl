import click
import json
from rich.emoji import Emoji
from rich.text import Text
from rich.syntax import Syntax

from pyintelowl.pyintelowl import IntelOwl


class ClickContext(click.Context):
    obj: IntelOwl
    """
    IntelOwl instance
    """


def get_status_text(status: str):
    styles = {
        "pending": ("#CE5C00", str(Emoji("gear"))),
        "running": ("#CE5C00", str(Emoji("gear"))),
        "reported_without_fails": ("#73D216", str(Emoji("heavy_check_mark"))),
        "reported_with_fails": ("#CC0000", str(Emoji("warning"))),
        "failed": ("#CC0000", str(Emoji("cross_mark"))),
    }
    color, emoji = styles[status]
    return Text(status + " " + emoji, style=color)


def get_success_text(success):
    success = str(success)
    styles = {
        "True": ("#73D216", str(Emoji("heavy_check_mark"))),
        "False": ("#CC0000", str(Emoji("cross_mark"))),
    }
    color, emoji = styles[success]
    return Text(emoji, style=color)


def get_json_syntax(obj):
    return Syntax(
        json.dumps(obj, indent=2),
        "json",
        theme="ansi_dark",
        word_wrap=True,
        tab_size=2,
    )


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options
