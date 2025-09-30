# Digit Problems

Digit problems are a series of problems that break an integer into its base-10 digits and apply some rule to those digits.

### Some common patterns

- Sums/products of digits: sum of digits, product of digits, sum of squares/cubes, etc.
- Digit factorial/power sums: numbers equal to $\sum f(d_i)$ for a per-digit function f (factorial, k-th power…).

### Classic upper-bound trick ($\sum f(d_i)$)

If f is applied per digit and f(9) is the max value per digit, then for any k-digit number:

- Max possible sum is $k \cdot f(9)$, min possible k-digit is $10^{k-1}$.
- $10^{k-1}$ grows faster than $k \cdot f(9)$
- If $k \cdot f(9) < 10^{k-1}$, no k-digit solution exists.

#### p30: Digit n Powers

Find the sum of all the numbers that can be written as the sum of n powers of their digits.

```
def digit_n_powers(n):
    pow_d = [d ** n for d in range(10)] # [0^n, 1^n, 2^n, ..., 9^n]
    NINE_N = 9 ** n   # 9^n

    # find the upper bound for k-digit number
    k, upper = 1, 0
    while k * NINE_N >= 10 ** (k - 1):
        upper = k * NINE_N
        k += 1

    return sum(
        x for x in range(2, upper + 1)
        if x == sum(pow_d[ord(c) - ord('0')] for c in str(x))
    )
```

#### p34: Digit Factorial:

Find the numbers and the sum of the numbers which are equal to the sum of the factorial of their digits.

```
import math
def digitFactorial():
    ans = {
        'sum': 0,
        'numbers': []
    }
    n, k = 10, 2
    # classic upper-bound trick
    while k * math.factorial(9) >= 10 ** (k - 1):
        if sum([math.factorial(int(num)) for num in str(n)]) == n:
            ans['sum'] += n
            ans['numbers'].append(n)
        n += 1
        k = len(str(n))
    return ans


```
