from __future__ import annotations

import pytest

from brainfy.intepreter import Interpreter


@pytest.mark.parametrize(('length', 'columns'), [
    (1, [0]),
    (5, [0, 0, 0, 0, 0]),
])
def test_given_interpreter_length_expected_same_columns(length, columns):
    assert Interpreter(length=length).columns == columns

