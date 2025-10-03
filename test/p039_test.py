from problem.p039_integer_right_triangles import int_right_triangles

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("int_right_triangles(500)",420), 
     ("int_right_triangles(800)", 720), 
     ("int_right_triangles(900)", 840), 
    ("int_right_triangles(1000)", 840)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected