from problem.p035_circular_primes import circular_primes

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("circular_primes(100)", 13), 
    ("circular_primes(100000)", 43),
    ("circular_primes(250000)", 45),
    ("circular_primes(500000)", 49),
    ("circular_primes(750000)", 49),
    ("circular_primes(1000000)", 55)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected