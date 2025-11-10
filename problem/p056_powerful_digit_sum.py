# A googol ( 10^100) is a massive number: one followed by one-hundred zeros;  100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form,  a^b, where a, b < n, what is the maximum digital sum?

# brute force
def powerful_digit_dum(n):
    ans = 0
    for a in range(n):
        for b in range(n):
            p = a ** b
            digit_total = sum(map(int, str(p)))
            ans = max(digit_total, ans)
    return ans