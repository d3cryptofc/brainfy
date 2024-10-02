from __future__ import annotations

from types import SimpleNamespace
from typing import Iterator, TextIO

from .traceback import Traceback

SCRIPT_MAXSIZE = 1024 * 1024

Tokens = SimpleNamespace(
    PLUS='+',
    MINUS='-',
    GREATER='>',
    LESS='<',
    DOT='.',
    HASH='#',
    BRACKET_START='[',
    BRACKET_END=']',
    NEWLINE='\n'
)


def tokenize(file: TextIO) -> Iterator[tuple[Traceback, str]]:
    is_comment = False
    line_counter = 1
    column_counter = 0

    for _ in range(SCRIPT_MAXSIZE):
        # Read one char.
        char = file.read(1)
        column_counter += 1

        # If char is empty
        if not char:
            break

        # If char is a new line.
        if char == Tokens.NEWLINE:
            is_comment = False
            line_counter += 1
            column_counter = 0
            continue

        # If char is not a token.
        if char not in Tokens.__dict__.values():
            continue

        # If char is a hash.
        if char == Tokens.HASH:
            is_comment = True

        # If was marked as comment.
        if is_comment:
            continue

        yield (Traceback(line=line_counter, column=column_counter), char)
