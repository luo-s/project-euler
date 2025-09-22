# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a given gridSize?

# dp approach
def latticePaths(n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n][n]

# more general case: m * n grid
def uniquePaths(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m][n]