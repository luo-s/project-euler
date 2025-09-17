# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

# smallestMult(5) should return 60.
# smallestMult(7) should return 420.
# smallestMult(10) should return 2520.
# smallestMult(13) should return 360360.
# smallestMult(20) should return 232792560.

############################################################
# python comes with a built-in function return the least common multiple
import math
def smallestMult(n):
    return math.lcm(*(range(1, n + 1)))

############################################################
# lcm(a, b) * gcd(a, b) = a * b 
def smallestMult(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i / gcd(ans, i)
    return ans
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

############################################################
# Prime Factorization: The LCM of two integer is the product of the each prime factors with the greatest power.

from collections import Counter
def smallestMult(n):
    ans = 1
    for i in range(1, n + 1):
        ans = lcm(ans, i)
    return ans

def prime_factors_count(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return Counter(factors)

def lcm(a, b):
    # Count prime factors
    count_a = prime_factors_count(a)
    count_b = prime_factors_count(b)

    # Take max exponent for all primes
    all_factors = count_a | count_b  # Union keeps max counts

    # Compute product
    lcm_val = 1
    for prime, exp in all_factors.items():
        lcm_val *= prime ** exp

    return lcm_val