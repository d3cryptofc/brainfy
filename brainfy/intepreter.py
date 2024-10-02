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

