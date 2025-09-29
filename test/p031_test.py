from problem.p031_coin_sums import coin_sums

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("coin_sums(50)", 451), 
    ("coin_sums(100)", 4563),
    ("coin_sums(150)", 21873),
    ("coin_sums(200)", 73682)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected