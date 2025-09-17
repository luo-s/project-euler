# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.

# specialPythagoreanTriplet(24) should return 480.
# specialPythagoreanTriplet(120) should return 49920, 55080 or 60000.
# specialPythagoreanTriplet(1000) should return 31875000.
                
def specialPythagoreanTriplet(n: int):
    for a in range(1, n // 3):                       # a < n/3
        for b in range(a + 1, (n - a) // 2 + 1):     # b < (n - a)/2
            c = n - a - b
            if a * a + b * b == c * c:                      
                return a * b * c
    return None