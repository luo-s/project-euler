from problem.p048_self_powers import self_powers

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("self_powers(10, 3)",317), 
     ("self_powers(150, 6)",29045),
     ("self_powers(673, 7)",2473989),
    ("self_powers(1000, 10)", 9110846700)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected