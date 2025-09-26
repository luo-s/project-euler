from problem.p024_lexi_permutations import nth_permutation

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("nth_permutation(699999)", 1938246570), 
    ("nth_permutation(899999)", 2536987410),
    ("nth_permutation(900000)", 2537014689),
    ("nth_permutation(999999)", 2783915460)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected