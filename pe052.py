#!/usr/bin/env python3
'''
Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

from itertools import count

if __name__ == '__main__':
    for integer in count(1):
        if (set(str(integer)) == set(str(integer * 2)) ==
                set(str(integer * 3)) == set(str(integer * 4)) ==
                set(str(integer * 5)) == set(str(integer * 6))):
            print(integer)
            break
