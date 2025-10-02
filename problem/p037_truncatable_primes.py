# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only n (8 ≤ n ≤ 11) primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def truncatable_primes(n):
    cnt, total = 0, 0
    i = 11  # start from 2-digit integer & skip even number
    while cnt < n:
        if is_truncatable_prime(i):
            cnt += 1
            total += i
        i += 2
    return total

# All subsequent digits must be from {1,3,7,9}
# the first digit could be {2, 3, 5, 7} e.g. 23, 53
def is_truncatable_prime(n):
    s = str(n)
    # quick check: optional
    if set('24680') & set(s[1:]):
        return False
    if sum(int(c) for c in s) % 3 == 0: 
        return False
    # check all truncated number
    l = len(s)
    trunc = {n}
    for i in range(1, l):
        trunc.add(int(s[:i]))
        trunc.add(int(s[i:]))
    for i in trunc:
        if not is_prime(i):
            return False
    return True

############################################################
def is_truncatable_prime(n: int) -> bool:
    if n < 10 or not is_prime(n):  # exclude 2,3,5,7 and composites
        return False
    s = str(n)
    # left-to-right truncations
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])): return False
    # right-to-left truncations
    for i in range(len(s) - 1, 0, -1):
        if not is_prime(int(s[:i])): return False
    return True

import math    
def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False

    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True