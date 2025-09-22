from problem.p015_lattice_paths import latticePaths

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("latticePaths(4)", 70), 
    ("latticePaths(9)", 48620),
    ("latticePaths(20)", 137846528820)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected
    