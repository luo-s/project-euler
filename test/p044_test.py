from problem.p044_pentagon_numbers import pentagon_num

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("pentagon_num()",5482660)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected