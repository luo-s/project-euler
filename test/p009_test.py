from problem.p009_special_pythagorean_triplet import specialPythagoreanTriplet

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("specialPythagoreanTriplet(24)", (480,)), 
    ("specialPythagoreanTriplet(120)", (49920, 55080, 60000)),
    ("specialPythagoreanTriplet(1000)", (31875000,))])

def test_eval(test_input, expected):
    assert eval(test_input) in expected