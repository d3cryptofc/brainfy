from __future__ import annotations

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

