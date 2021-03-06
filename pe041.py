#!/usr/bin/env python3
'''
Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''

from prime import primes

PANDIGITAL_SETS = {n: frozenset(str(i) for i in range(1, n + 1))
                   for n in range(1, 10)}


def is_pandigital(num):
    string = str(num)
    return set(string) == PANDIGITAL_SETS[len(string)]


# The largest possible pandigital number is 987,654,321.  However no nine-digit
# pandigital number is prime, as the sum of the digits 1-9 is 45, so all such
# numbers can be divided by 9.  The same applies to eight-digit pandigital
# numbers.
#
# So a sketch design presents itself: generate primes up to 7,654,321, then
# return the largest of these that is also pandigital.

if __name__ == '__main__':
    print(next(prime for prime in reversed(list(primes.range(7654321)))
               if is_pandigital(prime)))
