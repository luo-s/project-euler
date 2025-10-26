from problem.p047_distinct_prime_factors import distinct_prime_factor

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("distinct_prime_factor(2, 2)",14), 
     ("distinct_prime_factor(3, 3)",644),
    ("distinct_prime_factor(4, 4)", 134043)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected