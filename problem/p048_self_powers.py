# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# no overflow for integers in python
def self_powers(power, last_digits):
    total = 0
    for i in range(1, power + 1):
        total += pow(i, i)
    return total % (10 ** last_digits)

# improve version: mod calculation
def self_powers(power, last_digits):
    mod = 10 ** last_digits
    total = 0
    
    for i in range(1, power + 1):
        total = (total + pow(i, i, mod)) % mod
    
    return total

