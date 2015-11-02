#!/usr/bin/env python3
'''
Sum square difference

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''
from sys import argv

# The sum of the integers from 1 to n is n(n+1)/2, so the square of the sum is
# pretty easy to calculate.
#
# It makes sense, then, that there might be a formula for the sum of the
# squares.  Take a look at the first few values:
#
#     f(0) = 0
#     f(1) = 1
#     f(2) = 1 + 4 = 5
#     f(3) = 1 + 4 + 9 = 14
#     f(4) = 1 + 4 + 9 + 16 = 30
#
# Looks like f(n) = f(n-1) + n^2.  At the suggestion of the overview sheet, it
# makes sense that f would be quadratic, so just try plugging in some numbers
# and solving:
#
#     f(n) := an^3 + bn^2 + cn + d
#
# ...at which point I get bored of the maths, which I can do but just isn't
# very challenging, and jump to the solution.

if __name__ == '__main__':
    try:
        target = int(argv[1])
    except IndexError:
        target = 100

    # Triangle numbers.  I can remember this formula at least!  Use // to get
    # integer division; we know it'll be an integer anyway and it means we
    # don't need to worry about floats confusing anything.
    square_sum = (target * (target + 1) // 2) ** 2

    sum_square = target * (2 * target + 1) * (target + 1) // 6

    print(square_sum - sum_square)
