from problem.p040_champernownes_constant import champernowne_constant

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("champernowne_constant(100)",5), 
     ("champernowne_constant(1000)", 15), 
    ("champernowne_constant(1000000)", 210)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected