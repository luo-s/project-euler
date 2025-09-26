from problem.p025_digit_fibo import digit_fibo

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("digit_fibo(5)", 21), 
    ("digit_fibo(10)", 45),
    ("digit_fibo(15)", 69),
    ("digit_fibo(20)", 93)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected
    