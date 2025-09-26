# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under n.

def sum_amicable_num(n):
    divisor_map = {}
    total = 0
    # start from 2 to avoid amicable pair (0, 1)
    for i in range(2, n):
        sum = divisor_map[i] = divisor_sum(i)
        if sum in divisor_map and divisor_map[sum] == i and i != sum:
            total = total + divisor_map[i] + i
    return total

def divisor_sum(n):
    if n == 1: return 0
    total, i = 1, 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
        i += 1
    return total


    