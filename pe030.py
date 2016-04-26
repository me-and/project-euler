#!/usr/bin/env python3
'''
Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
'''

from itertools import count
from sys import argv

# Let fp(k) be the sum of the pth powers of the digits of k, so for example
#
#     f4(1634) = 1634
#     fp(1000) = 1 for all p
#
# The smallest n-digit number is 10 ^ (n-1), since we ignore initial zeros.
#
# The largest value of fp(k) where k is an n-digit number is n * (9 ^ p).
#
# The largest value of fp(k) is thus linear with respect to n, while the
# smallest possible n-digit number is exponential.
#
# Considering fourth powers of n-digit numbers k, we therefor know that, given
# values of n, for f4(k) == k to hold, k must be in the following ranges:
#
#     n = 2:     10 ≤ k ≤ 13122
#     n = 3:    100 ≤ k ≤ 19683
#     n = 4:   1000 ≤ k ≤ 26244
#     n = 5:  10000 ≤ k ≤ 32805
#     n = 6: 100000 ≤ k ≤ 39366
#
# Thus in the case of the fourth powers we know k must be at most a five-digit
# number, since there are no six-digit numbers less than 39366.  Further, we
# know when k is at most a five-digit number, f4(k) ≤ 32805, so since we are
# interested in cases where f4(k) == k, we only need to find cases where
# k ≤ 32805.

if __name__ == '__main__':
    try:
        power = int(argv[1])
    except IndexError:
        power = 5

    powers = {str(n): n ** power for n in range(10)}

    # Find the maximum number we're interested in.
    for digits in count(2):
        maximum = digits * (9 ** power)
        minimum = 10 ** (digits - 1)
        if maximum < minimum:
            maximum = (digits - 1) * (9 ** power)
            break

    running_total = 0
    for number in range(10, maximum + 1):
        power_sum = sum(powers[n] for n in str(number))

        if number == power_sum:
            running_total += number
            print(number)

    print('Total:', running_total)
