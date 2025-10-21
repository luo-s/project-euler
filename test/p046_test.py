from problem.p046_goldbach_other_conjecture import goldbach

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("goldbach()",5777)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected