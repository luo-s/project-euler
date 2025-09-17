from problem.p006_sum_square_difference import sumSquareDifference

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("sumSquareDifference(10)", 2640), 
    ("sumSquareDifference(20)", 41230),
    ("sumSquareDifference(100)", 25164150)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected