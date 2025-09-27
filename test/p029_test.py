from problem.p029_distinct_powers import distinct_powers

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("distinct_powers(15)", 177), 
    ("distinct_powers(20)", 324),
    ("distinct_powers(25)", 519),
    ("distinct_powers(30)", 755)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected