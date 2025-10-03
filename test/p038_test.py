from problem.p038_pandigital_multiples import pandigital_multiples

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("pandigital_multiples(8)", 78156234), 
    ("pandigital_multiples(9)", 932718654)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected