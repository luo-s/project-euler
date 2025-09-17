## Check for Prime Numbers

### Brute Force (Basic Trial Division)

The most straightforward way to check is to follow the definition of prime number: test all numbers from $2$ up to $n − 1$. This approach is slow with $O(n)$ Time and $O(1)$ space.

```
def isPrime(n):
    if n <= 1:
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

def isPrime(n):
    if n <= 1:
        return False

    # Check divisibility from 2 to the square root of n
    for i in range(2, math.isqrt(n) + 1):
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

### [Miller–Rabin Primality Test (Fast for Large n)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

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

### [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

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
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False

    # Extract all primes
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes
```
