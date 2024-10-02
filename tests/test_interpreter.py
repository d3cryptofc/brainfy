from __future__ import annotations

import pytest

from brainfy.intepreter import Interpreter


@pytest.mark.parametrize(('length', 'columns'), [
    (1, [0]),
    (5, [0, 0, 0, 0, 0]),
])
def test_given_interpreter_length_expected_same_columns(length, columns):
    assert Interpreter(length=length).columns == columns


@pytest.mark.parametrize(('increases', 'expected'), [
    (1, 1),
    (255, 255),
    (256, 0)
])
def test_increase_must_increase_column_value(increases, expected):
    i = Interpreter(length=1)
    for _ in range(increases):
        i.increase()
    assert i.value == expected

