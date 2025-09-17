# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the nth prime number?

# nthPrime(6) should return 13.
# nthPrime(10) should return 29.
# nthPrime(100) should return 541.
# nthPrime(1000) should return 7919.
# nthPrime(10001) should return 104743.

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

