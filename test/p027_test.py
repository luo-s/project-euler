from problem.p027_quadratic_primes import quadratic_primes

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("quadratic_primes(200)", -4925), 
    ("quadratic_primes(500)", -18901),
    ("quadratic_primes(800)", -43835),
    ("quadratic_primes(1000)", -59231)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected