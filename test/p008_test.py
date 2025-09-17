from problem.p008_largest_product import largestProductinaSeries

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("largestProductinaSeries(4)", 5832),
    ("largestProductinaSeries(13)", 23514624000)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected