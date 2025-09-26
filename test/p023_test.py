from problem.p023_non_abundant_sum import non_abundant_sum

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("non_abundant_sum(10000)", 3731004), 
    ("non_abundant_sum(15000)", 4039939),
    ("non_abundant_sum(20000)", 4159710),
    ("non_abundant_sum(28213)", 4179871)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected