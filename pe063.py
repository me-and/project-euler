#!/usr/bin/env python3
'''
Powerful digit counts

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

# Excluding 1^1 (which meets the criteria but is clearly a special case), we
# know the base for any such numbers must be in the range 2-9, since 1^n only
# has one digit, and 10^n has n+1 digits.  Further, since 10^n has n+1 digits,
# and is the lowest possible n+1-digit number, we know 9^n has at most n digits.
#
# Further, the number of digits in 9^n is at most log10(9^n) + 1.  That's
# equivalent to n * log10(9) + 1 ≈ 0.954n + 1.  Thus we know that there exists k
# such that for all n ≥ k, b^n has fewer than n digits.  We just need to find
# that value, and count.  There are ways to be cleverer, but frankly this
# solution is quick enough anyway.

from itertools import count, product
from math import floor, log10


def digits(x):
    return floor(log10(x)) + 1


if __name__ == '__main__':
    for k in count(2):
        if digits(9 ** k) < k:
            break

    print(sum(digits(b ** n) == n for b, n in
              product(range(1, 10), range(1, k))))
