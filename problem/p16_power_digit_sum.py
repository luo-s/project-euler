# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^n?
# integer will never overflow in python!

def power_digit_sum(n):
    p = 2 ** n
    ans = 0
    while p > 0:
        ans += p % 10
        p //= 10
    return ans