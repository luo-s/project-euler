from problem.p050_consecutive_prime_sum import consecutive_prime_sum

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("consecutive_prime_sum(100)",41), 
     ("consecutive_prime_sum(1000)",953),
    ("consecutive_prime_sum(1000000)", 997651)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected