# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import Fraction
def digit_cancelling():
    prod = Fraction(1, 1)
    for i in range(10, 99):
        for j in range(i + 1, 100):
            if j % 10 == 0 or i % 10 == 0:
                continue
            si, sj = str(i), str(j)
            if si[0] == sj[0] and Fraction(int(si[1]), int(sj[1])) == Fraction(i, j):
                prod *= Fraction(i, j)
            elif si[0] == sj[1] and Fraction(int(si[1]), int(sj[0])) == Fraction(i, j):
                prod *= Fraction(i, j)
            elif si[1] == sj[0] and Fraction(int(si[0]), int(sj[1])) == Fraction(i, j):
                prod *= Fraction(i, j)
            elif si[1] == sj[1] and Fraction(int(si[0]), int(sj[0])) == Fraction(i, j):
                prod *= Fraction(i, j)
    return prod.denominator

############################################################
# without using fractions library
import math
def digit_cancelling():
    num_prod = den_prod = 1
    for i in range(10, 99):
        for j in range(i + 1, 100):
            si, sj = str(i), str(j)
            if si[1] == '0' and sj[1] == '0':
                continue
            if si[0] == sj[0] and sj[1] != '0' and i * int(sj[1]) == j * int(si[1]):
                num_prod *= i; den_prod *= j
            elif si[0] == sj[1] and sj[0] != '0' and i * int(sj[0]) == j * int(si[1]):
                num_prod *= i; den_prod *= j
            elif si[1] == sj[0] and sj[1] != '0' and i * int(sj[1]) == j * int(si[0]):
                num_prod *= i; den_prod *= j
            elif si[1] == sj[1] and sj[0] != '0' and i * int(sj[0]) == j * int(si[0]):
                num_prod *= i; den_prod *= j
    g = math.gcd(num_prod, den_prod)
    return den_prod // g