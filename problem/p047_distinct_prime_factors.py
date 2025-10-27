# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

# first n consecutive intefers to have m distinct prime factors each.

def prime_factors_set(x: int) -> set:
    """Return the set of prime factors of x."""
    s = set()
    d = 2
    while d * d <= x:
        while x % d == 0:
            s.add(d)
            x //= d
        d += 1 if d == 2 else 2  # small speedup: skip evens after 2
    if x > 1:
        s.add(x)
    return s

def has_n_distinct_pf(x: int, n: int) -> bool:
    return len(prime_factors_set(x)) == n

def distinct_prime_factor(n: int, m: int) -> int:
    """Return the first k with m consecutive integers each having n distinct prime factors."""
    k = 2
    streak = 0
    while True:
        if has_n_distinct_pf(k, n):
            streak += 1
            if streak == m:
                return k - m + 1
        else:
            streak = 0
        k += 1