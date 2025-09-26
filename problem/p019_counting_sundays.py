# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# make the 1900/01/01 the first day, counting since then, every 7 days is a Sunday (n % 7 == 0)
def counting_sundays(start, end):
    # calculate the day count of Jan 01 of the start year
    day_start = 1
    year = start - 1900
    for i in range(year):
        day_start += 365     
        day_start += 1 if (i + 1) % 4 == 0 else 0
    
    # count the multiple of 7 of first day of each month
    GAP = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0
    while start <= end:
        if start % 4 == 0 and start != 1900:
            for i in LEAP:
                count += 1 if day_start % 7 == 0 else 0
                day_start += i
        else:
            for i in GAP:
                count += 1 if day_start % 7 == 0 else 0
                day_start += i
        start += 1
    return count

