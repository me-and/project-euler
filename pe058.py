#!/usr/bin/env python3
'''
Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

    *37*  36   35   34   33   32  *31*
     38  *17*  16   15   14  *13*  30
     39   18  * 5*   4  * 3*  12   29
     40   19    6    1    2   11   28
     41   20  * 7*   8    9   10   27
     42   21   22   23   24   25   26
    *43*  44   45   46   47   48   49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
'''

from prime import MillerRabinPrimes


def generate_corners():
    increment = 10
    side_length = 2
    value = 3
    while True:
        # Don't yield the fourth corner, as it's always going to be a perfect
        # square and thus never prime.
        yield (value, value + side_length, value + side_length * 2)
        value += increment
        side_length += 2
        increment += 8

if __name__ == '__main__':
    num_corners = 1
    num_primes = 0
    side_length = 1

    primes = MillerRabinPrimes()

    for corners in generate_corners():
        num_corners += 4
        side_length += 2
        num_primes += sum(corner in primes for corner in corners)
        if num_primes * 10 < num_corners:
            print(side_length)
            break
