# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-length digit pandigital prime that exists?
import math
import itertools
def pandigitalPrime(n):
    perms = list(itertools.permutations(range(1, n + 1)))
    for i, p in enumerate(perms):
        perms[i] = int(''.join(map(str, p)))
    perms.sort(reverse=True)
    for p in perms:
        if is_prime(p):
            return p
    return None

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
