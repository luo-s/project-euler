from problem.p003_largest_prime_factor import largestPrimeFactor

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("largestPrimeFactor(2)", 2), 
    ("largestPrimeFactor(3)", 3), 
    ("largestPrimeFactor(5)", 5), 
    ("largestPrimeFactor(7)", 7), 
    ("largestPrimeFactor(8)", 2),
    ("largestPrimeFactor(13195)", 29),
    ("largestPrimeFactor(600851475143)", 6857)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected