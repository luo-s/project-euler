from problem.p053_combinatoric_selections import combinatoric_selections

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("combinatoric_selections(1000)",4626), 
     ("combinatoric_selections(10000)",4431),
     ("combinatoric_selections(100000)",4255),
    ("combinatoric_selections(1000000)", 4075)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected