from __future__ import annotations

from typing import TextIO

from .parser import parse_brackets
from .tokenizer import Tokens, tokenize


class Interpreter:
    def __init__(self, length: int = 20) -> None:
        self.__length = length

        if not isinstance(length, int):
            msg = '`length` parameter must be an integer.'
            raise TypeError(msg)

        if not (0 < length < 100):
            msg = 'the range of the integer `length` must be between 0-100'
            raise ValueError(msg)

        self.__columns = [0] * length
        self.__pointer = 0

    def __repr__(self):
        return (
            '{}<'
            'pointer={!r}, '
            'decimal={!r}, '
            'ascii={!r}, '
            'length={!r}'
            '>'
        ).format(
            type(self).__name__,
            self.pointer,
            self.decimal,
            self.ascii,
            self.__length
        )

    @property
    def decimal(self) -> int:
        return self.__columns[self.__pointer]

    @property
    def ascii(self) -> int:
        return chr(self.decimal)

    @property
    def pointer(self) -> int:
        return self.__pointer

    @property
    def columns(self) -> list[int]:
        return self.__columns.copy()

    def _update_value(self, *, up: bool) -> None:
        pointer = self.__pointer
        columns = self.__columns
        value = columns[pointer]

        if up and value >= 255:
            columns[pointer] = 0
        elif up:
            columns[pointer] += 1

        if not up and value <= 0:
            columns[pointer] = 255
        elif not up:
            columns[pointer] -= 1

    def increase(self) -> None:
        self._update_value(up=True)

    def decrease(self) -> None:
        self._update_value(up=False)

    def forward(self) -> None:
        if self.__pointer < self.__length:
            self.__pointer += 1
        else:
            self.__pointer = 0

    def previous(self) -> None:
        if self.__pointer > 0:
            self.__pointer -= 1
        else:
            self.__pointer = self.__length - 1

    def run(self, file: TextIO) -> None:
        script_tokens = list(tokenize(file))
        script_tokens_length = len(script_tokens)

        bracket_position_map = parse_brackets(script_tokens)

        running = True
        cursor = 0

        while running:
            _, token = script_tokens[cursor]

            if token == Tokens.PLUS:
                self.increase()
            elif token == Tokens.MINUS:
                self.decrease()
            elif token == Tokens.GREATER:
                self.forward()
            elif token == Tokens.LESS:
                self.previous()
            elif token == Tokens.DOT:
                print(self.ascii, end='')
            elif (token == Tokens.BRACKET_START and self.decimal == 0
                or token == Tokens.BRACKET_END and self.decimal != 0):
                cursor = bracket_position_map[cursor]

            if cursor + 1 <= script_tokens_length - 1:
                cursor += 1
            else:
                running = False
