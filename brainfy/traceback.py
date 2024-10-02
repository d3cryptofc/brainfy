from dataclasses import dataclass


@dataclass(frozen=True)
class Traceback:
    line: int
    column: int
