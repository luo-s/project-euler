# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2 × 1^2
# 15 = 7 + 2 × 2^2
# 21 = 3 + 2 x 3^2
# 25 = 7 + 2 x 3^2
# 27 = 19 + 2 x 2^2
# 33 = 31 + 2 x 1^2
# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math

def goldbach():
    n = 9 # first odd composite number
    while True: 
        if is_prime(n):
            n += 2
            continue
        # get all primes smaller than n
        primes = sieve_of_eratosthenes(n)
        # check conjecture
        found = False
        for p in primes:
            k = n - p
            if k % 2 == 0:
                square = k // 2
                if math.sqrt(square).is_integer():
                    found = True
                    break
        if not found: 
            return n
        n += 2

def is_prime(n):
    if n < 2:
        return False

    # Check divisibility from 2 to the square root of n
    limit = math.isqrt(n)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False

    return True

def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    # Initialize all numbers as potential primes
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Sieve process
    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if is_prime[p]:
            # Mark multiples of p as False (composite)
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Extract all primes
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes