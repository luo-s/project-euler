# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, such that multiplied by integers  {2,3,…,n}
#  , contain the same digits.

def permuted_multiples(n):
    num = 1
    while True:
        k = 2
        while k < n + 1:
            multiple = num * k
            if sorted(list(str(num))) != sorted(list(str(multiple))):
                break
            if k == n:
                return num
            k += 1
        num += 1
             

def permuted_multiples(n):
    num = 1
    while True:
        # Check if num * k for all k in [2, n] are permutations of num
        for k in range(2, n + 1):
            if sorted(str(num)) != sorted(str(num * k)):
                break
        else:
            # If we never broke out of the loop, all multiples matched
            return num
        num += 1