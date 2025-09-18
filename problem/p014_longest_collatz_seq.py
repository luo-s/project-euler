# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under the given limit, produces the longest chain?

# Note: Once the chain starts the terms are allowed to go above limit.

# longestCollatzSequence(14) should return 9.
# longestCollatzSequence(5847) should return 3711.
# longestCollatzSequence(46500) should return 35655.
# longestCollatzSequence(54512) should return 52527.
# longestCollatzSequence(100000) should return 77031.
# longestCollatzSequence(1000000) should return 837799.

# recursive approach
def longestCollatzSequence(n):
    longest_length = 0
    starting_number = 1
    memo = {}

    for i in range(1, n + 1):  # Start from 1, not 0
        l = collatzSeq(i, memo)
        if l > longest_length:
            longest_length = l
            starting_number = i
    
    return starting_number

def collatzSeq(n, memo={}):
    # memoization
    if n in memo:
        return memo[n]
    
    # Base case
    if n == 1:
        memo[n] = 1
        return 1
    
    # Recursive case
    if n % 2 == 0:
        length = collatzSeq(n // 2, memo) + 1
    else:
        length = collatzSeq(3 * n + 1, memo) + 1
    
    # Store result before returning
    memo[n] = length
    return length
