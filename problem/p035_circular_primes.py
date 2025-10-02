# The number 197 is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below n, whereas 100 ≤ n ≤ 1000000?

# Note:

# Circular primes individual rotation can exceed n.

# some quick check:
# 1) if the number contains digit 0,2,4,6,8, one of its rotations can be divided by 2;
# 2) if the sum of all digits is divided by 3, it is divided by 3;
# 3) if the number contains 5, one of its rotations can be divided by 5.
# Thus, this number can only contains: 1, 3, 7, 9.

import math
def circular_primes(n):
    count = 0
    for num in range(n + 1):
        if num in [2,3,5,7]:
            count += 1
            continue
        digits = list(map(int, str(num)))
        # check for divisor 2:
        if set([2,4,6,8,0]) & set(digits) : continue
        # check for divisor 3
        if sum(digits) % 3 == 0: continue
        # check for divisor 5:
        if 5 in digits: continue
        # check for all rotations
        flag = True
        k = len(digits)
        double_digits = digits + digits
        rotations = []
        for i in range(k):
            rotations.append(double_digits[i:i + k])
        for rotation in rotations:
            number = int("".join(map(str, rotation)))
            if not is_prime(number): 
                flag = False
                break
        if flag is True:
            count += 1
    return count
        
############################################################

import math
def circular_primes(n):
    count = 0
    for num in range(n + 1):
        if num in (2, 3, 5, 7):
            count += 1
            continue
        digits = set(str(num))
        # check for 2 & 5
        if digits & set('246805'): continue
        # check for 3
        if sum(map(int, str(num))) % 3 == 0: continue
        # check for all rotations
        if all(is_prime(r) for r in rotations_of(num)):
            count += 1
    return count

# yield: turn function into a generator
def rotations_of(n: int):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:] + s[:i])


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