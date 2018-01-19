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

from itertools import combinations_with_replacement, count
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
#
# That all said, note that fp(123) == fp(321).  It turns out to be quicker to
# only consider unique sets of digits of k, thus avoiding calculating both
# fp(123) and fp(321), then working out whether the digits of k can be
# rearranged to make fp(k).

if __name__ == '__main__':
    try:
        power = int(argv[1])
    except IndexError:
        power = 5

    powers = {n: n ** power for n in range(10)}

    # Find the maximum number of digits that we're interested in.
    for num_digits in count(2):
        maximum = num_digits * (9 ** power)
        minimum = 10 ** (num_digits - 1)
        if maximum < minimum:
            break
    num_digits -= 1

    running_total = 0
    for digits in combinations_with_replacement(range(10), num_digits):
        power_sum = sum(powers[x] for x in digits)
        if power_sum < 10:
            # Don't care about numbers less than 10, because the sum isn't a
            # sum.
            continue

        # To check whether there's an arrangement of the digits of k such that
        # fp(k) == k, use the fact that combinations_with_replacement gives
        # tuples that are already sorted.  Thus we convert fp(k) to a string,
        # sort the string character-by-character, then convert the digits back
        # to individual integers.
        if digits == tuple(map(
                int,
                sorted('{:0{digits}}'.format(power_sum, digits=num_digits)))):
            running_total += power_sum

    print(running_total)
