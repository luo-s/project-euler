from problem.p021_amicable_numbers import sum_amicable_num

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("sum_amicable_num(1000)", 504), 
    ("sum_amicable_num(2000)", 2898),
    ("sum_amicable_num(5000)", 8442),
    ("sum_amicable_num(10000)", 31626)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected