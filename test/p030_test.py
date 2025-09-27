from problem.p030_digit_n_powers import digit_n_powers

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("digit_n_powers(2)", 0), 
    ("digit_n_powers(3)", 1301),
    ("digit_n_powers(4)", 19316),
    ("digit_n_powers(5)", 443839)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected