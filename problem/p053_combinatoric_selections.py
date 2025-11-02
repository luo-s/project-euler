# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation,  C(5, 3)=10
 

# In general,  C(n, r)= n! / r!(n − r)! where r≤n, n! = n×(n−1)×...×3×2×1, and 0!=1.

# It is not until n=23 that a value exceeds one-million: C(23, 10) = 1144066.

# How many, not necessarily distinct, values of C(n, r) for 1 ≤ n ≤ 100 are greater than one-million?

# brute force
import math
def combinatoric_selections(k):
    count = 0
    for n in range(2, 101):
        for r in range(1, n + 1):
            combination = math.comb(n, r)
            if combination > k:
                count += 1
    return count

# improved version
def combinatoric_selections(k):
    count = 0
    for n in range(2, 101):   
        for r in range(1, n // 2 + 1):
            combination = math.comb(n, r)
            if combination > k:
                # symmetry in combination
                count += (n - r) - r + 1
                break
    return count