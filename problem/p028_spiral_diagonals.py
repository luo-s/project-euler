# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in an n by n spiral formed in the same way?

# in up-right direction: i^2 for i % 2 == 1 and i <= n
def spiral_diagonals(n):
    ans = 1
    for i in range(3, n + 1, 2):
        sq = i ** 2
        ans += sq                   # up-right direction
        ans += sq - (i - 1)         # up-left direction
        ans += sq - 2 * (i - 1)     # down-left direction
        ans += sq - 3 * (i - 1)     # down-right direction
    return ans
