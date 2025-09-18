from problem.p014_longest_collatz_seq import longestCollatzSequence

import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("longestCollatzSequence(14)", 9), 
    ("longestCollatzSequence(5847)", 3711),
    ("longestCollatzSequence(46500)", 35655),
    ("longestCollatzSequence(54512)", 52527),
    ("longestCollatzSequence(100000)", 77031),
    ("longestCollatzSequence(1000000)", 837799)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected