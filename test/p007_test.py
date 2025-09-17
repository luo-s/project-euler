from problem.p007_nth_prime import nthPrime

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("nthPrime(6)", 13), 
    ("nthPrime(10)", 29),
    ("nthPrime(100)", 541),
    ("nthPrime(1000)", 7919),
    ("nthPrime(10001)", 104743)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected