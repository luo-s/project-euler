from problem.p016_power_digit_sum import power_digit_sum

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("power_digit_sum(15)", 26), 
    ("power_digit_sum(128)", 166),
    ("power_digit_sum(1000)", 1366)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected