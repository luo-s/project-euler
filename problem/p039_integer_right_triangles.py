# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ n, is the number of solutions maximized?

# a^2 + b^2 = c^2, a <= b <= c, a + b > c 
# a + b + c = p (p <= n)
# find p that have the maximum solutions of integer set (a, b, c)?
def int_right_triangles(n):
    ma, ans = 0, 0
    for p in range(3, n):
        count = 0
        for a in range(1, p // 2):
            for b in range(a, p // 2):
                c = p - a - b
                if c < b:  # keep non-decreasing order: a ≤ b ≤ c
                    continue
                if a * a + b * b == c * c:
                    count += 1
        if count > ma:
            ma, ans = count, p
    return ans
