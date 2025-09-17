from problem.p004_largest_palindrome_product import largestPalindromeProduct

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("largestPalindromeProduct(2)", 9009), 
    ("largestPalindromeProduct(3)", 906609)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected