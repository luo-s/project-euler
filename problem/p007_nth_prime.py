# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the nth prime number?

# nthPrime(6) should return 13.
# nthPrime(10) should return 29.
# nthPrime(100) should return 541.
# nthPrime(1000) should return 7919.
# nthPrime(10001) should return 104743.

############################################################
# Python prime library https://pypi.org/project/primePy/ 
# primePy is slow
from primePy import primes
def nthPrime(n):
    return primes.first(n)[-1]

############################################################
# syspy library https://www.sympy.org/en/index.html
from sympy import prime
def nthPrime(n):
    return prime(n)

############################################################
# brute force
def nthPrime(n):
    if n == 2: return 2 # handle 2 separately to skip unnecessary numbers
    i, count = 3, 1 
    while count < n:
        if isPrime(i):
            count += 1
        i += 2
    return i - 2

import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

############################################################
# we can use sieve of Eratosthenes when knowing the upper bound of nth prime
import math

def upper_bound(n: int) -> int:
    # p_n ≤ n(ln n + ln ln n) for n>= 6
    if n < 6:
        return 15
    return int(n * (math.log(n) + math.log(math.log(n))) ) + 10  # small cushion

def sieve(n):
    if n < 2:
        return []

    # Initialize all numbers as potential primes
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Sieve process
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            # Mark multiples of p as False (composite)
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False

    # Extract all primes
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

def nthPrime(n):
    if n == 1:
        return 2
    bound = upper_bound(n)
    primes = sieve(bound)
    # If the cushion under-shoots (rare), expand and retry.
    while len(primes) < n:
        bound = int(bound * 1.2) + 1
        primes = sieve(bound)
    return primes[n - 1]