from problem.p034_digit_factorial import digitFactorial

import pytest

@pytest.mark.parametrize(
        "test_input, expected",
        [("digitFactorial()", {'sum': 40730, 'numbers': [145, 40585]})])

def test_eval(test_input, expected):
    assert eval(test_input) == expected