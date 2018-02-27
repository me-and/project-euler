#!/usr/bin/env python3
'''
Cubic permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
'''

from itertools import count, permutations
from math import factorial
from sys import argv

from polygons import cubes


def count_cube_permutations(number):
    # Count the size of the set, to avoid double-counting identical permutations
    # that result from multiple identical digits in the original number.
    #
    # itertools.permutations returns a tuple that needs to be joined together
    # before it can be tested for whether it's a cube.
    return len(set(string for string in permutations(str(number)) if string[0] != '0' and int(''.join(string)) in cubes))


def inverse_factorial(num):
    '''Smallest x such that x! >= num'''
    return next(x for x in count(1) if factorial(x) >= num)


if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 5

    # To avoid checking cubes that are clearly too small, work out the minimum
    # before which there are insufficient digits to hit the requisite number of
    # permutations.
    start_digits = inverse_factorial(target)

    print(next(number for number in cubes.range(10 ** (start_digits - 1), None) if count_cube_permutations(number) == target))
