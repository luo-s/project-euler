from problem.p041_pandigital_prime import pandigitalPrime

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("pandigitalPrime(4)",4231), 
    ("pandigitalPrime(7)", 7652413)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected