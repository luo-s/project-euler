from problem.p017_number_letter_count import number_letter_count
from problem.p017_number_letter_count import num_char_cnt

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("number_letter_count(5)", 19), 
    ("number_letter_count(150)", 1903),
    ("number_letter_count(1000)", 21124),
    ("num_char_cnt(5)", 19), 
    ("num_char_cnt(150)", 1903),
    ("num_char_cnt(1000)", 21124)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected