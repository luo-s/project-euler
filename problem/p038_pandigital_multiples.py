# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192 192 × 2 = 384 192 × 3 = 576
 
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).

# What is the largest 1 to k pandigital k-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?

# brute force: approximately 30s
# time complexity: O(10**k * k)
def pandigital_multiples(k):
    lower_limit = 10 ** (k - 1)
    uppper_limit = 10 ** k - 1
    # loop through DESC for possible k-digit number
    for num in range(uppper_limit, lower_limit - 1, -1):
        if is_pan_multi(num, k):
            return num
    return 0

def is_pan_multi(n, k):
    s = str(n)
    if set(s) != set('123456789'[:k]):
        return False
    for i in range(1, k):
        unit = int(s[:i])
        if not s.startswith(str(unit)):
            continue
        t = ''
        multiple = 1
        while len(t) < k:
            t += str(unit * multiple)
            if not s.startswith(t):
                break
            multiple += 1
        if s == t and multiple > 2:
            return True
    return False


    
