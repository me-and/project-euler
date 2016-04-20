#!/usr/bin/env python3
'''
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).  If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt

from divisors import divisors


def is_amicable_pair(x, y):
    if x == y:
        return False
    else:
        return sum(divisors(x)) == y and sum(divisors(y)) == x


if __name__ == '__main__':
    divisor_sums = {}
    for i in range(1, 10000):
        divisor_sums[i] = sum(divisors(i))

    amicable_numbers = set()
    for k, v in divisor_sums.items():
        if k != v:
            try:
                possible_pair = divisor_sums[v]
            except KeyError:
                pass
            else:
                if possible_pair == k:
                    amicable_numbers.add(k)
                    amicable_numbers.add(v)

    print(sum(amicable_numbers))
