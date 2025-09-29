# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can n pence be made using any number of coins?

# let dp[i] be differnet number of ways to get i pence
# Count all the ways you can make i - coin and then add the current coin.

def coin_sums(n):
    COIN = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in COIN:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    return dp[n]

# let dfs(i, c) denote the # of ways to get amount c with the first i coins. 
# dfs(i, c) = dfs(i - 1, c) + dfs(i, c - COIN[i])
    # 1) if we use the ith coin: dfs(i - 1, c)
    # 2) if we don't use the ith coin: dfs(i, c - COIN[i])

from functools import lru_cache
def coin_sums(n):
    COIN = [1, 2, 5, 10, 20, 50, 100, 200]
    @lru_cache
    
    def dfs(i, c):
        if i < 0: 
            return 1 if c == 0 else 0
        # same as if c < 0: return 0
        if c < COIN[i]:
            return dfs(i - 1, c)
        return dfs(i - 1, c) + dfs(i, c - COIN[i])
    
    return dfs(len(COIN) - 1, n)

# memoization without functools lib
def coin_sums(n):
    COIN = [1, 2, 5, 10, 20, 50, 100, 200]
    memo = {}  # key: (i, c), value: number of ways
    
    def dfs(i, c):
        # If already computed, return cached value
        if (i, c) in memo:
            return memo[(i, c)]
        # Base cases
        if i < 0:
            return 1 if c == 0 else 0
        if c < 0:
            return 0
        # Compute result: skip coin i or use coin i
        result = dfs(i - 1, c) + dfs(i, c - COIN[i])
        # Store in memo before returning
        memo[(i, c)] = result
        return result
    
    return dfs(len(COIN) - 1, n)