#!/usr/bin/env python3
'''
Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''

from prime import primes


def prime_triples():
    for prime_one in primes.range(1000, 9999):
        for prime_two in primes.range(prime_one + 1, 9999):
            if prime_two + (prime_two - prime_one) in primes:
                # Arithmetic sequence of primes.
                yield prime_one, prime_two, prime_two + (prime_two - prime_one)


def count_chars(string):
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    return counts


def permutations(prime_one, prime_two, prime_three):
    return (count_chars(str(prime_one)) == count_chars(str(prime_two)) ==
            count_chars(str(prime_three)))


if __name__ == '__main__':
    for prime_one, prime_two, prime_three in prime_triples():
        if permutations(prime_one, prime_two, prime_three):
            string = str(prime_one) + str(prime_two) + str(prime_three)
            if string != '148748178147':
                print(string)
