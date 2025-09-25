# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ONES = {
    0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
    10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8
}
TENS = {20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}  
HUNDRED = 7      # "hundred"
AND = 3          # "and"
SCALES = [       # (value, len("name"))
    (10**9, 7),  # billion
    (10**6, 7),  # million
    (10**3, 8),  # thousand
]

def number_letter_count(limit: int) -> int:
    return sum(count_number(i) for i in range(1, limit + 1))

def _under_100(n: int) -> int:
    if n < 20:
        return ONES[n]
    tens, once = divmod(n, 10)
    return TENS[tens * 10] + ONES[once]

def _under_1000(n: int) -> int:
    if n < 100:
        return _under_100(n)
    hundreds, last_2digits = divmod(n, 100)
    total = ONES[hundreds] + HUNDRED
    if last_2digits:
        total += AND + _under_100(last_2digits)  # British "and"
    return total

def count_number(n: int) -> int:
    if n == 0:
        return 0 
    total, remaining = 0, n

    # Handle billions/millions/thousands
    for scale_val, name_len in SCALES:
        if remaining >= scale_val:
            chunk, remaining = divmod(remaining, scale_val)
            total += _under_1000(chunk) + name_len
            # British style often includes "and" when the remainder is < 100
            # after a higher scale (e.g., "one thousand and one").
            if 0 < remaining < 100:
                total += AND
                
    # Final sub-1000 chunk
    total += _under_1000(remaining)
    return total