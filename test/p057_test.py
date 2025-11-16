from problem.p057_sqrt_convergents import sqrt_convergents

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("sqrt_convergents(10)",1), 
     ("sqrt_convergents(100)",15),
    ("sqrt_convergents(1000)", 153)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected