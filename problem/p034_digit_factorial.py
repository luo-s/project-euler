# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the numbers and the sum of the numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# for a k-digit number, 
# 1) the largest sum of factorial is k * 9! must >= 10^(k-1).
import math
def digitFactorial():
    ans = {
        'sum': 0, 
        'numbers': []
    }
    n, k = 10, 2
    while k * math.factorial(9) >= 10 ** (k - 1):
        if sum([math.factorial(int(c)) for c in str(n)]) == n:
            ans['sum'] += n
            ans['numbers'].append(n)
        n += 1
        k = len(str(n))
    return ans 
        