# The sum of the squares of the first ten natural numbers is,

# 1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10) ** 2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

# sumSquareDifference(10) should return 2640.
# sumSquareDifference(20) should return 41230.
# sumSquareDifference(100) should return 25164150.

# brute force
def sumSquareDifference(n):
    sum = ss = 0
    for i in range(1, n + 1):
        sum += i
        ss += pow(i, 2)
    return pow(sum, 2) - ss

# math
def sumSquareDifference(n):
    square_of_sum = pow((n * (n + 1) / 2), 2)
    sum_of_square = n * (n + 1) * (2 * n + 1) / 6
    return  square_of_sum - sum_of_square 
