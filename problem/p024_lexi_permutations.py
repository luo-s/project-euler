# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# 
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210

# What is the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# the 1st is 0123456789, the last is 9876543210, there are 10! = 3628800 total numbers
import math
def nth_permutation(n):
    digits = list(range(10))
    result = []

    for i in range(9, -1, -1):
        fact = math.factorial(i)
        index = n // fact
        n %= fact
        result.append(digits.pop(index))

    return int("".join(map(str, result)))
