'''
Functions for working with primes
'''

from itertools import count
from collections import defaultdict


def prime_generator():
    '''
    Generate primes reasonably efficiently.
    '''
    # This function is an implementation of an incremental Sieve of
    # Eratosthenes, based broadly on the algorithm by Richard Bird, as
    # described in O'Neill, Milssa E, "The Genuine Sieve of Eratosthenes",
    # <http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf>, accessed 21 August
    # 2015, and apparently published in the Journal of Functional Programming
    # (2009) 19, pp 95-106, doi: 10.1017/S0956796808007004.
    composites = defaultdict(list)
    x = 1
    while True:
        x += 1
        if x in composites:
            gens = composites.pop(x)
            for gen in gens:
                composites[next(gen)].append(gen)
        else:
            gen = count(x * 2, x)
            composites[next(gen)].append(gen)
            yield x


def prime_factors(n):
    '''
    Give the prime factors of a number.
    '''
    factors = defaultdict(int)
    primes = prime_generator()
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
        if p ** 2 > n:
            if n != 1:  # Happens if the original n was prime.
                factors[n] += 1
            return factors
