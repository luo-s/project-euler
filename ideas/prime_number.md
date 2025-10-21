## Check for Prime Numbers

### Brute Force (Basic Trial Division)

The most straightforward way to check is to follow the definition of prime number: test all numbers from $2$ up to $n − 1$. This approach is slow with $O(n)$ Time and $O(1)$ space.

```
def isPrime(n):
    if n < 2:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
```

### Basic Trial Division with optimization

Since factors always come in pairs, we only need to check up to sqrt(n).
This approach is slow with $O(\sqrt{n})$ Time and $O(1)$ space.

```
import math

def is_prime(n):
    if n < 2:
        return False

    # Check divisibility from 2 to sqrt(n)
    limit = math.isqrt(n)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False

    return True
```

### Best Trial Division

Every prime number above 3 can be written as $6k \pm 1$. This complexcity rstays $O(\sqrt{n})$ but with fewer divisions.

```
import math

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
```

### [Miller–Rabin Primality Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

Miller–Rabin Primality Test is a probabilistic primality test, but with selected bases, it becomes deterministic for 32-bit or 64-bit integers. The time complexity drops to $O(\log^3 n)$.

```
def is_prime_mr(n):
    if n < 2:
        return False

    # small primes
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p

    # write n-1 as 2^s * d
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # deterministic bases for 64-bit numbers
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
```

## Find Prime Numbers

### Find Prime Numbers with a Given Limit: [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

The sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit. Time complexity $O(n \log \log n)$, Space complexity $O(n)$.

```
import math

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
```

### Find the nth Prime Number

- Brute Force Method: count prime number 1 by 1

```
def nthPrime(n):
    if n == 2: return 2 # handle 2 separately to skip unnecessary numbers
    i, count = 3, 1
    while count < n:
        if isPrime(i):
            count += 1
        i += 2
    return i - 2

import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
```

- We need a upper bond to use the Sieve of Eratosthenes
  - In math, we know the upper bound for nth prime is: p_n ≤ n(ln n + ln ln n) for n>= 6

```
import math

def upper_bound(n: int) -> int:
    if n < 6:
        return 15
    return int(n * (math.log(n) + math.log(math.log(n))) ) + 10  # small cushion

def sieve(n):
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

def nthPrime(n):
    if n == 1:
        return 2
    bound = upper_bound(n)
    primes = sieve(bound)
    # If the cushion under-shoots (rare), expand and retry.
    while len(primes) < n:
        bound = int(bound * 1.2) + 1
        primes = sieve(bound)
    return primes[n - 1]
```
