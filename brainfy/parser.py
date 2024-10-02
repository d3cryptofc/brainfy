from __future__ import annotations

from .tokenizer import Tokens
from .traceback import Traceback


def extra_start_bracket_exception(traceback: Traceback):
    msg = "Extra backet '[' at line {}, column {}.".format(
        traceback.line,
        traceback.column
    )
    return RuntimeError(msg)


def extra_end_bracket_exception(traceback: Traceback):
    msg = "Extra backet ']' at line {}, column {}.".format(
        traceback.line,
        traceback.column
    )
    return RuntimeError(msg)


def parse_brackets(tokens: list[tuple(int, str)]) -> dict[int, int]:
    start_position_stack = []
    all_positions_map = {}

    for index, (traceback, token) in enumerate(tokens):
        if token == Tokens.BRACKET_START:
            start_position_stack.append((traceback, index))
        elif token == Tokens.BRACKET_END:
            if not start_position_stack:
                raise extra_end_bracket_exception(traceback)

            start_bracket_position = start_position_stack.pop()
            end_bracket_position = index

            all_positions_map[start_bracket_position[1]] = end_bracket_position
            all_positions_map[end_bracket_position] = start_bracket_position[1]

    if start_position_stack:
        raise extra_start_bracket_exception(start_position_stack[0][0])

    return all_positions_map
