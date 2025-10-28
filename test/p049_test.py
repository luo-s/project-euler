from problem.p049_prime_permutations import prime_permutations

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("prime_permutations()",296962999629)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected