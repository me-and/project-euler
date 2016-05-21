#!/usr/bin/env python3
'''
Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

# For an n-digit number, the minimum sum of factorials of digits is n, and the
# maximum is n * 9!.  Given 8 * 9! = 2,903,040, there can be no eight-digit
# numbers that are curious, because the highest sum of factorials of digits has
# only seven digits (and as the number of digits increases, the maximum sum of
# factorials of digits increases linearly, while the numbers themselves
# increase exponentially).
#
# Thus we have an upper bound of 7 * 9!.

from math import factorial as fact
from sys import argv

if __name__ == '__main__':
    running_sum = 0
    print(sum(i for i in range(10, 7 * fact(9) + 1)
              if i == sum(fact(int(d)) for d in str(i))))
