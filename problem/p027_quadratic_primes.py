# Euler discovered the remarkable quadratic formula: n^2+n+41

# It turns out that the formula will produce 40 primes for the consecutive integer values  0 ≤ n ≤ 39. However, when n=40,40 ^2 + 40 + 41= 40(40+1) + 41 is divisible by 41, and certainly when n=41,41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n^2 + an + b, where |a| < range and |b| ≤ range, where |n|is the modulus/absolute value of n. (e.g. |11| = 11 and |−4| = 4)
 
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

# brute force
import math
def quadratic_primes(limit):
    prod = longest = 0
    for a in range(-limit + 1, limit):
        for b in range(-limit, limit + 1):
            count = n = 0
            quad = n ** 2 + a * n + b
            while is_prime(quad):
                count += 1
                n += 1
                quad = n ** 2 + a * n + b
            if count > longest:
                longest = count
                prod = a * b
    return prod

def is_prime(n):
    if n <= 1:
        return False
    # Check divisibility from 2 to the square root of n
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# math approach
# n^2 + an + b is prime, 
# start n == 0: b has to be a prime number. sieve prime numbers <= limit

def quadratic_primes(limit):
    PRIMES = sieve_of_eratosthenes(limit)
    prod = longest = 0
    for b in PRIMES:
        for a in range(-limit + 1, limit):
            count = n = 1   # quad is automatic prime when n = 0
            quad = n ** 2 + a * n + b
            while is_prime(quad):
                count += 1
                n += 1
                quad = n ** 2 + a * n + b
            if count > longest:
                longest = count
                prod = a * b
    return prod

def sieve_of_eratosthenes(n):
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