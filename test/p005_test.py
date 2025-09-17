from problem.p005_smallest_multiple import smallestMult

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("smallestMult(5)", 60), 
    ("smallestMult(7)", 420),
    ("smallestMult(10)", 2520),
    ("smallestMult(13)", 360360),
    ("smallestMult(20)", 232792560)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected