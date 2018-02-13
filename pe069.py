#!/usr/bin/env python3
'''
Totient maximum

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

n   Relatively Prime  φ(n)  n/φ(n)
2   1                 1     2
3   1,2               2     1.5
4   1,3               2     2
5   1,2,3,4           4     1.25
6   1,5               2     3
7   1,2,3,4,5,6       6     1.1666...
8   1,3,5,7           4     2
9   1,2,4,5,7,8       6     1.5
10  1,3,7,9           4     2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

from collections import deque
from sys import argv

from prime import primes
from sequence import MonatonicIncreasingSequence

# From Wikipedia: Euler's product formula: φ(n) = n * Π_{p|n}(1-1/p), where p|n
# denotes the prime numbers dividing n.  For example:
#
#     φ(36) = φ(2^2 * 3^2) = 36 * (1 - ½) * (1 - ⅓) = 36 * ½ * ⅔ = 12
#
# However, taking this further (at the suggestion of the Project Euler overview
# solution for this problem):
#
#        φ(n) = n * Π_{p|n}(1-1/p)
#
#     => n/φ(n) = 1/Π_{p|n}(1-1/p) = Π_{p|n}(p/(p-1))
#
# To calculate n/φ(n), then, it is only necessary to consider p|n, not n
# directly, and therefore the exponents in the prime factorisation of n are
# irrelevant.  Further, note that p/(p-1) is monotonically decreasing as p
# increases for p > 1.
#
# Consider n, and a prime q that doesn't divide n.  It follows that q*n/φ(q*n) =
# n/φ(n) * q/(q-1), and thus that q*n/φ(q*n) > n/φ(n).
#
# Given these facts, we know that if n_k is the product of the k smallest
# primes, then for all n < n_k, n/φ(n) < n_k/φ(n_k).
#
# Finally, then, the solution is simply the largest product of consecutive
# primes starting from 2 that fits within the given maximum.


def prime_product():
    product = 1
    for prime in primes:
        product *= prime
        yield product


prime_products = MonatonicIncreasingSequence(prime_product())


# Based in part on the tail recipe in the Python itertools documentation.
def last(iterable):
    '''Return the final element of an iterator'''
    return deque(iterable, maxlen=1)[0]


if __name__ == '__main__':
    try:
        maximum = int(argv[1])
    except IndexError:
        maximum = 1000000

    print(last(prime_products.range(maximum)))
