# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the given number?

# largestPrimeFactor(2) should return 2.
# largestPrimeFactor(3) should return 3.
# largestPrimeFactor(5) should return 5.
# largestPrimeFactor(7) should return 7.
# largestPrimeFactor(8) should return 2.
# largestPrimeFactor(13195) should return 29.
# largestPrimeFactor(600851475143) should return 6857.

# brute force: time consuming for checking every possivle factor and prime number one by one
import math
def largestPrimeFactor(n):
    lpf = 1
    for i in range(n, 1, -1):
        if n % i == 0 and isPrime(i) is True:
            return i
    return lpf

# prime number identify function
def isPrime(n):
    if n == 2: return True
    m = math.isqrt(n)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


# n //= i: prime factorization, and n becomes small quickly
def largestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# with optimization (handle the special prime number separately)
import math
def largestPrimeFactor(n):
    # Remove factors of 2
    while n % 2 == 0:
        n //= 2
        lpf = 2
    
    # Try odd factors up to sqrt(n)
    i = 3
    while i <= math.isqrt(n):
        while n % i == 0:
            n //= i
            lpf = i
        i += 2
    
    # If n > 2, it's prime
    if n > 2:
        lpf = n
    
    return lpf