from problem.p045_triangular_pentagonal_hexagonal import tri_pen_hex

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("tri_pen_hex(40756)",1533776805)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected