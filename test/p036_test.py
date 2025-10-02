from problem.p036_double_base_palindromes import db_base_palindromes

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("db_base_palindromes(1000)", 1772), 
    ("db_base_palindromes(50000)", 105795),
    ("db_base_palindromes(500000)", 286602),
    ("db_base_palindromes(1000000)", 872187)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected