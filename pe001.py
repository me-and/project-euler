#!/usr/bin/env python3
'''
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from itertools import takewhile

def multiple_generator():
    num = 1
    while True:
        if (num % 3) == 0 or (num % 5) == 0:
            yield num
        num += 1

if __name__ == '__main__':
    print(sum(takewhile(lambda x: x < 1000, multiple_generator())))
