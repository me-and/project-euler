#!/usr/bin/env python3
'''
Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
'''

from functools import reduce
from itertools import count
from math import sqrt
from sys import argv

from prime import prime_factors_seed


def triangle(x):
    return (x * (x + 1)) // 2


def num_divisors(x, pg_seed=None):
    # Based on http://mathschallenge.net/index.php?section=faq&ref=number/number_of_divisors
    prime_factors, pg_seed = prime_factors_seed(x, pg_seed,
                                                preserve_seed=False)
    return (reduce(lambda x, y: x * (y + 1),
                   prime_factors.values(),
                   1),
            pg_seed)


if __name__ == '__main__':
    try:
        goal = int(argv[1])
    except IndexError:
        goal = 500

    pg_seed = None

    # Start at 2, since num_divisors doesn't work with 1.
    for i in count(2):
        num = triangle(i)
        divisors, pg_seed = num_divisors(num, pg_seed)
        if divisors > goal:
            print(num)
            break
