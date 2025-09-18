# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below n.

# primeSummation(17) should return 41.
# primeSummation(2001) should return 277050.
# primeSummation(140759) should return 873608362.
# primeSummation(2000000) should return 142913828922.

# sieve of Eratosthenes
import math
def primeSummation(n):
    if n < 2: return 0
    isPrime = [True] * n              
    isPrime[0] = isPrime[1] = False
    limit = math.isqrt(n)
    for p in range(2, limit):
        if isPrime[p]:
            for multiple in range(p * p, n, p):
                isPrime[multiple] = False
    primes = [i for i, prime in enumerate(isPrime) if prime]
    return sum(primes)
