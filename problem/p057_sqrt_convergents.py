# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# sqrt(2)= 1 + 1/(2 + 1/(2 + 1/(2 + …)))

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5

# 1 + 1/(2 + 1/2)) = 7/5 = 1.4

# 1 + 1/(2 + 1/(2 + 1/2))) = 17/12 = 1.41666...

# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379

# The next three expansions are  99/70, 239/169, and 577/408.
# But the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first n expansions, how many fractions contain a numerator with more digits than denominator?

from fractions import Fraction 
def sqrt_convergents(n):
    count = 0
    start = Fraction(2, 1)
    for _ in range(n):
        start = 2 + Fraction(1, start)
        convergent = start - 1
        if len(str(convergent.numerator)) > len(str(convergent.denominator)):
            count += 1
    return count
