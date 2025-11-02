# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an n prime value family.

from itertools import combinations
import sympy as sp

def prime_digit_replacements(target):   # target = how many primes you want, e.g. 8
    for p in sp.primerange(2, 2_000_000):  # big enough for Euler 51
        s = str(p)
        L = len(s)
        # choose positions to replace
        for r in range(1, L):
            for pos in combinations(range(L), r):
                # the digits we replace must already be the SAME in the original number
                first = s[pos[0]]
                if any(s[i] != first for i in pos):
                    continue

                family = []
                for d in '0123456789':
                    if pos[0] == 0 and d == '0':
                        continue  # no leading zero

                    chars = list(s)
                    for i in pos:
                        chars[i] = d
                    candidate = int(''.join(chars))   # <-- don't overwrite `target`

                    if sp.isprime(candidate):
                        family.append(candidate)

                if len(family) >= target:
                    return p