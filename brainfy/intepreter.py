from __future__ import annotations


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

    @property
    def value(self) -> int:
        return self.__columns[self.__pointer]

    @property
    def pointer(self) -> int:
        return self.__pointer

    @property
    def columns(self) -> list[int]:
        return self.__columns

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
