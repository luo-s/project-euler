# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < n for which 1/d contains the longest recurring cycle in its decimal fraction part.

def reciprocal_cycles(n):
    longest, ans = 0, 1
    for d in range(2, n):
        cycle = cnt(d)
        if cycle > longest:
            longest = cycle
            ans = d
    return ans

def cnt(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    if n == 1: return 0
    # find the smallest k that 10^k ≡ 1 (mod n)
    k, mod = 1, 10 % n
    while mod != 1:
        mod = (mod * 10) % n
        k += 1
    return k
