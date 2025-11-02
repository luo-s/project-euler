from problem.p052_permuted_multiples import permuted_multiples

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("permuted_multiples(2)",125874), 
    ("permuted_multiples(6)", 142857)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected