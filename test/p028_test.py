from problem.p028_spiral_diagonals import spiral_diagonals

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("spiral_diagonals(101)", 692101), 
    ("spiral_diagonals(303)", 18591725),
    ("spiral_diagonals(505)", 85986601),
    ("spiral_diagonals(1001)", 669171001)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected