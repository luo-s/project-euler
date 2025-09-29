from problem.p032_pandigital_products import pandigital_products

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("pandigital_products(4)", 12), 
    ("pandigital_products(6)", 162),
    ("pandigital_products(7)", 0),
    ("pandigital_products(8)", 13458),
    ("pandigital_products(9)", 45228)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected