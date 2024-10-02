from __future__ import annotations

import pytest

from brainfy import Interpreter


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
    assert i.decimal == expected


@pytest.mark.parametrize(('decreases', 'expected'), [
    (1, 255),
    (2, 254),
    (255, 1),
    (256, 0)
])
def test_decrease_must_decrease_column_value(decreases, expected):
    i = Interpreter(length=1)
    for _ in range(decreases):
        i.decrease()
    assert i.decimal == expected


@pytest.mark.parametrize(('forwards', 'expected'), [
    (0, 0),
    (5, 5),
    (10, 10),
    (11, 0)
])
def test_forward_must_move_pointer_to_forward_column(forwards, expected):
    i = Interpreter(length=10)
    for _ in range(forwards):
        i.forward()
    assert i.pointer == expected


@pytest.mark.parametrize(('previous', 'expected'), [
    (0, 0),
    (1, 9),
    (5, 5),
])
def test_previous_must_move_pointer_to_previous_column(previous, expected):
    i = Interpreter(length=10)
    for _ in range(previous):
        i.previous()
    assert i.pointer == expected
