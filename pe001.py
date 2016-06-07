#!/usr/bin/env python3
'''
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from itertools import takewhile, count

from sequence import MonatonicIncreasingSequence

multiples = MonatonicIncreasingSequence(n for n in count()
                                        if n % 3 == 0 or n % 5 == 0)

if __name__ == '__main__':
    print(sum(multiples.range(999)))
