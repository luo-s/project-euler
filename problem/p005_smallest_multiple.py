# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

# smallestMult(5) should return 60.
# smallestMult(7) should return 420.
# smallestMult(10) should return 2520.
# smallestMult(13) should return 360360.
# smallestMult(20) should return 232792560.

# python comes with a built-in function return the least common multiple
import math
def smallestMult(n):
    return math.lcm(*(range(1, n + 1)))

# lcm(a, b) * gcd(a, b) = a * b 
def smallestMult(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i / gcd(ans, i)
    return ans
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a