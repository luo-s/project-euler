# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers.

# largestPalindromeProduct(2) should return a number.
# largestPalindromeProduct(2) should return 9009.
# largestPalindromeProduct(3) should return 906609.

############################################################
# brute force: check every single possible product
def largestPalindromeProduct(n):
    hi, lo = pow(10, n) - 1, pow(10, n-1)
    ans = 0
    for i in range(hi, lo - 1, -1):
        for j in range(hi, lo - 1, -1):
            if isPalindrome(i * j):
                ans = max(ans, i * j)
    return ans

############################################################
# optimized version (pruned double loop) 
def largestPalindromeProduct(n):
    hi, lo = pow(10, n) - 1, pow(10, n-1)
    best = 0
    for i in range(hi, lo - 1, -1):
        # If even i*hi can't beat current best, we're done
        if i * hi <= best:
            break
        for j in range(i, lo - 1, -1):  # j starts at i to avoid duplicates
            prod = i * j
            if prod <= best:
                break  # decreasing j only makes prod smaller
            if isPalindrome(prod):
                best = prod
                break  # for this i, no smaller j will give a larger prod
    return best

############################################################
# assistant function: check palindrome
def isPalindrome(n):
    s = str(n)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]  # Compare string with its reverse
