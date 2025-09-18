from problem.p010_sum_of_primes import primeSummation

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("primeSummation(17)", 41), 
    ("primeSummation(2001)", 277050),
    ("primeSummation(140759)", 873608362),
    ("primeSummation(2000000)", 142913828922)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected