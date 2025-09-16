# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

# multiples_of_3_or_5(10) should return 23
# multiples_of_3_or_5(49) should return 543.
# multiples_of_3_or_5(1000) should return 233168.
# multiples_of_3_or_5(8456) should return 16687353.
# multiples_of_3_or_5(19564) should return 89301183.

def multiples_of_3_or_5(n):
    ans = 0
    for i in range(n):
        if i % 3 == 0:
            ans += i
        elif i % 5 == 0:
            ans += i
    return ans
