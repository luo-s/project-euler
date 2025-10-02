from problem.p037_truncatable_primes import truncatable_primes

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("truncatable_primes(8)", 1986), 
    ("truncatable_primes(9)", 5123),
    ("truncatable_primes(10)", 8920),
    ("truncatable_primes(11)", 748317)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected