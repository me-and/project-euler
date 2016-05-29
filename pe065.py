#!/usr/bin/env python3
'''
Convergents of e

The square root of 2 can be written as an infinite continued fraction.

    √2 = 1 +          1
             -------------------
             2 +        1
                 ---------------
                 2 +      1
                     -----------
                     2 +    1
                         -------
                         2 + ...

The infinite continue fraction can be written √2 = [1;(2)], (2) indicates that
2 repeats ad infinitum.  In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for
square roots provides the best rational approximations.  Let us consider the
convergents for √22.

        1   3
    1 + - = -
        2   2

          1
    1 + -----   7
            1 = -
        2 + -   5
            2

            1
    1 + ---------
              1     17
        2 + ----- = --
                1   12
            2 + -
                2

              1
    1 + -------------
                1
        2 + ---------   41
                  1   = --
            2 + -----   29
                    1
                2 + -
                    2

Hence the sequence for the first ten convergents for √2 are:

    1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378,
    ...

What is most surprising is that the important mathematical constant,

    e = [2; 1,2,1, 1,4,1, 1,6,1, ..., 1,2k,1, ...]

The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of the digits in the numerator of the 10th convergent is 1+4+5+7 = 17.

Find the sum of the digits in the numerator of the 100th convergent of the
continued fraction for e.
'''

from fractions import Fraction
from itertools import islice
from sys import argv


def gen_terms():
    k = 2
    while True:
        yield 1
        yield k
        yield 1
        k += 2

if __name__ == '__main__':
    try:
        convergent = int(argv[1])
    except IndexError:
        convergent = 100

    terms = list(islice(gen_terms(), convergent - 1))
    result = Fraction(1, terms[-1])
    for term in terms[-2::-1]:
        result = Fraction(1, term + result)

    result += 2

    print(sum(int(c) for c in str(result.numerator)))
