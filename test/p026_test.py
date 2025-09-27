from problem.p026_reciprocal_cycles import reciprocal_cycles

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("reciprocal_cycles(700)", 659), 
    ("reciprocal_cycles(800)", 743),
    ("reciprocal_cycles(900)", 887),
    ("reciprocal_cycles(1000)", 983)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected