# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# two pointers
def consecutive_prime_sum(n):
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)
    
    left, right, l = 0, 0, len(primes)
    streak, max_streak, ans = 0, 0, 0
    while left < l:
        total = 0
        right = left
        while total <= primes[-1] and right < l:
            total += primes[right]
            if total in prime_set:
                streak = right - left + 1
                if streak > max_streak:
                    max_streak = streak
                    ans = total
            right += 1
        left += 1
    return ans


# presum
def consecutive_prime_sum(n):
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)

    # prefix[i] = sum of primes[0:i]
    prefix = [0]
    for p in primes:
        prefix.append(prefix[-1] + p)

    max_len = 0
    ans = 0
    L = len(primes)

    # try all start indices
    for i in range(L):
        # for each start, try longer and longer sequences
        # but stop if sum > n
        for j in range(i + max_len + 1, L + 1):
            total = prefix[j] - prefix[i]
            if total > n:
                break
            if total in prime_set:
                length = j - i
                if length > max_len:
                    max_len = length
                    ans = total
    return ans

import math
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