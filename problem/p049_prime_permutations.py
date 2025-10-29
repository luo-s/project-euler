# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

# brute force O(n^3) (49s)
import math
def prime_permutations():
    # all 4-digit primes
    primes = [p for p in sieve_of_eratosthenes(10000) if 1000 <= p < 10000]
    l = len(primes)
    for a in range(0, l - 2):
        for b in range(a + 1, l - 1):
            for c in range(b + 1, l):
                s1, s2, s3 = str(primes[a]), str(primes[b]), str(primes[c])
                if sorted(s1) == sorted(s2) == sorted(s3) and primes[b] - primes[a] == primes[c] - primes[b] and s1 != '1487':
                    return int(s1 + s2 + s3)

# optimized solution (0.01s)
from collections import defaultdict
def prime_permutations():
    # all 4-digit primes
    primes = [p for p in sieve_of_eratosthenes(10000) if 1000 <= p < 10000]

    # group by digit signature (sorted digits)
    groups = defaultdict(list)
    for p in primes:
        groups[''.join(sorted(str(p)))].append(p)

    for sig, grp in groups.items():
        if len(grp) < 3:
            continue
        grp.sort()
        s = set(grp)
        # look for 3-term arithmetic sequences p, q, r within the group
        for i in range(len(grp) - 1):
            p = grp[i]
            for j in range(i + 1, len(grp)):
                q = grp[j]
                r = 2*q - p
                if r in s:
                    # skip the known example from Euler (1487, 4817, 8147)
                    if (p, q, r) == (1487, 4817, 8147):
                        continue
                    return int(f"{p}{q}{r}")

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
            # start form p * p, since 2 * p, 3 * p, ... (p - 1) * p have already been marked when processing smaller primes
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Extract all primes
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes