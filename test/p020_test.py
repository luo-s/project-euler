from problem.p020_factorial_digit_sum import sum_factorial_digits

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("sum_factorial_digits(10)", 27), 
    ("sum_factorial_digits(25)", 72),
    ("sum_factorial_digits(50)", 216),
    ("sum_factorial_digits(75)", 432),
    ("sum_factorial_digits(100)", 648)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected