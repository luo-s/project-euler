# Greatest Common Divisor and Least Common Multiple

### Greatest Common Divisor(GCD)

Greatest common divisor of two positive integers is the largest positive integer that divides both numbers without remainder.

### How to Find GCD

1. Prime Factorization
   The GCD of two integer is the product of the common prime factors.

```
def prime_factors(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:   # Only need to check up to sqrt(n)
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:  # If n is prime and > 1 at the end, include it
        factors.append(n)
    return factors

def gcd(a, b):
    # Get prime factors of both numbers
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)

    # Common prime factors (consider multiplicity)
    common = []
    for p in factors_a:
        if p in factors_b:
            common.append(p)
            factors_b.remove(p)  # remove one occurrence to handle duplicates correctly

    # GCD is product of common prime factors
    gcd_val = 1
    for p in common:
        gcd_val *= p

    return gcd_val
```

In the code above, we take extra calculations to get a list of common prime factors. However, we don't need to keep track of the list, we only need to know the prime factors and their count. Thus we can use a dictionary to count prime factors, and it's much easier to get common factors.

```
from collections import Counter

def prime_factors_count(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return Counter(factors)

def gcd(a, b):
    # Count prime factors
    count_a = prime_factors_count(a)
    count_b = prime_factors_count(b)

    # Take min exponent for common primes
    common_factors = count_a & count_b  # Intersection keeps min counts

    # Compute product
    gcd_val = 1
    for prime, exp in common_factors.items():
        gcd_val *= prime ** exp

    return gcd_val
```

2. [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)

```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

### Least Common Multiple (LCM)

Least Common Multiple (LCM) of two integers is the smallest integer that is a multiple of both numbers.

### How to Find LCM

1. Prime Factorization
   The LCM of two integer is the product of the each prime factors with the greatest power.

```
from collections import Counter

def prime_factors_count(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return Counter(factors)

def lcm(a, b):
    # Count prime factors
    count_a = prime_factors_count(a)
    count_b = prime_factors_count(b)

    # Take max exponent for all primes
    all_factors = count_a | count_b  # Union keeps max counts

    # Compute product
    lcm_val = 1
    for prime, exp in all_factors.items():
        lcm_val *= prime ** exp

    return lcm_val
```

2. $lcm(a, b) \times gcd(a, b) = a \times b$

```
def lcm(a, b):
    return a * b / gcd(a, b)
```
