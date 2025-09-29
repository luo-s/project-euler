from problem.p033_digit_cancelling_fractions import digit_cancelling

import pytest

@pytest.mark.parametrize(
        "test_input, expected",
        [("digit_cancelling()", 100)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected