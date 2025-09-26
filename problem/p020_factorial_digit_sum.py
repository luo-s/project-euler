# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits n!

# integer will not overflow in python
import math
def sum_factorial_digits(n):
    fac = math.factorial(n)
    total = 0
    while fac > 0:
        total += fac % 10
        fac //= 10
    return total

# optimized with the string method
import math
def sum_factorial_digits(n):
    return sum(map(int, str(math.factorial(n))))