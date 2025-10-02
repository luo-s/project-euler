# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than n, whereas 1000 ≤ n ≤ 1000000, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def db_base_palindromes(n):
    total = 0
    for num in range(1, n):
        #  # find k so that 2**k >= 1_000_000
        k = 1
        while 2 ** k < 1000000:
            k += 1
        
        pow_2 = [2 ** i for i in range(k - 1, -1, -1)]

        # get the binary
        b, remaining = '', num
        for pow2 in pow_2:
            if remaining >= pow2:
                b += '1'
                remaining -= pow2
            else:
                b += '0'
        # remove leading 0s
        b = b.lstrip('0')
        # calculate the sum
        if is_palindromic(b) and is_palindromic(num):
            total += num
    return total

def is_palindromic(n):
    s = str(n)
    l = len(s)
    left, right = 0, l - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

############################################################
# built-in function bin(n)
def db_base_palindromes(n):
    total = 0
    # only loop odds: Even numbers always end in 0 in binary
    for num in range(1, n, 2): 
        # # binary without '0b'
        b = bin(num)[2:]    
        if is_palindromic(num) and is_palindromic(b):
            total += num
    return total

def is_palindromic(x) -> bool:
    s = str(x)
    return s == s[::-1]
