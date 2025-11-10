from problem.p056_powerful_digit_sum import powerful_digit_dum

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("powerful_digit_dum(3)",4), 
     ("powerful_digit_dum(10)",45),
     ("powerful_digit_dum(50)",406),
     ("powerful_digit_dum(75)",684),
    ("powerful_digit_dum(100)", 972)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected