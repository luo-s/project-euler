# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of n powers of their digits.

# what's the upper bound?
# for a k-digit number, the largest sum of n-th power of digits is k * 9^n
# and k * 9^n >= 10^(k - 1)
# different n will have different upper bound

def digit_n_powers(n):
    pow_d = [d ** n for d in range(10)] # [0^n, 1^n, 2^n, ..., 9^n]
    nine_n = pow_d[9]   # 9^n
    
    # find the upper bound
    k, upper = 1, 0
    while k * nine_n >= 10 ** (k - 1):
        upper = k * nine_n
        k += 1
    
    return sum(
        x for x in range(2, upper + 1)
        if x == sum(pow_d[ord(c) - ord('0')] for c in str(x))
    )