from problem.p017_number_letter_count import number_letter_count

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("number_letter_count(5)", 19), 
    ("number_letter_count(150)", 1903),
    ("number_letter_count(1000)", 21124)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected