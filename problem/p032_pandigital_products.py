# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through n pandigital.

# Hint: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def pandigital_products(n):
    if not (1 <= n <= 9):
        raise ValueError("n must be between 1 and 9 for decimal pandigital digits.")
    
    target = ''.join(str(d) for d in range(1, n + 1))
    pandigital = set()
    # max value of n is 9, it can only be 1-digit x 4-digit = 4-digit, or 2-digit x 3-digit = 4-digit, thus the max product is 9999
    for i in range(2, 10 ** 4):
        factors = factor_pairs(i)
        for factor in factors:
            string = str(i) + str(factor[0]) + str(factor[1])
            if len(string) != n: continue
            if '0' in string: continue
            number = ''.join(sorted(string))
            if number == target:
                pandigital.add(i)
    return sum(pandigital)

# get all pairs of factor except (1, n) and (sqrt(n), sqrt(n))
def factor_pairs(n):
    pairs = []
    i = 2
    while i * i < n:
        if n % i == 0:
            pairs.append((i, n // i))
        i += 1
    return pairs