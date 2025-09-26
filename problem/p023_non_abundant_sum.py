# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all positive integers <= n which cannot be written as the sum of two abundant numbers.

# brute force: get all abundant number < 28123, and try all possible pairs, sieve the number can be written as sum of two abundant numbers
def non_abundant_sum(n):
    # all abundant numbers < 28123
    abundant = [i for i in range(1, n + 1) if is_abundant(i)]

    can, l = [False] * (n + 1), len(abundant)
    for i in range(l):
        for j in range(i, l):
            s = abundant[i] + abundant[j]
            if s > n: break
            can[s] = True
    return sum(m for m in range(1, n + 1) if not can[m])    
            
def divisor_sum(n):
    if n == 1: return 0
    total, i = 1, 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
        i += 1
    return total

def is_abundant(n):
    return divisor_sum(n) > n