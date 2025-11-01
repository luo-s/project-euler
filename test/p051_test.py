from problem.p051_prime_digit_replacements import prime_digit_replacements

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("prime_digit_replacements(6)",13), 
     ("prime_digit_replacements(7)",56003),
    ("prime_digit_replacements(8)", 121313)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected