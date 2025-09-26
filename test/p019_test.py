from problem.p019_counting_sundays import counting_sundays

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("counting_sundays(1943, 1946)", 6), 
    ("counting_sundays(1995, 2000)", 10),
    ("counting_sundays(1901, 2000)", 171)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected