#!/usr/bin/env python3
'''
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

from itertools import count
from math import sqrt
from sys import argv


def triangle(x):
    return (x * (x + 1)) // 2


def divisors(x):
    # Based broadly on http://stackoverflow.com/a/171779/220155
    for i in range(1, int(sqrt(x) + 1)):
        if x % i == 0:
            yield i
            if i * i != x:
                yield x // i


def generator_len(gen):
    length = 0
    for _ in gen:
        length += 1
    return length


def num_divisors(x):
    return generator_len(divisors(x))


if __name__ == '__main__':
    try:
        goal = int(argv[1])
    except IndexError:
        goal = 500

    for i in count(1):
        num = triangle(i)
        if num_divisors(num) > goal:
            print(num)
            break
