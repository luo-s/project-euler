# problem/__init__.py
from problem.p1_multiples_of_3_or_5 import multiples_of_3_or_5

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("multiples_of_3_or_5(10)", 23), 
    ("multiples_of_3_or_5(49)", 543), 
    ("multiples_of_3_or_5(1000)", 233168), 
    ("multiples_of_3_or_5(8456)", 16687353), 
    ("multiples_of_3_or_5(19564)", 89301183)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected