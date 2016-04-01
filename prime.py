'''
Functions for working with primes
'''

from copy import deepcopy
from itertools import chain, count
from collections import defaultdict


class prime_generator(object):
    '''
    Generate primes reasonably efficiently.
    '''
    def __init__(self, seed=None, preserve_seed=True):
        if seed is None:
            self.primes = []
            self.composites = defaultdict(list)
            self._generator = self._prime_generator()
        else:
            # Use a previous prime generator object to seed this one, avoiding
            # the need to regenerate primes we've previously seen.
            if preserve_seed:
                # To ensure the seed keeps working as a prime number generator,
                # take copies of all the mutable things we care about.
                self.primes = seed.primes.copy()
                self.composites = deepcopy(seed.composites)
            else:
                # We can break the seed working as a prime number generator, so
                # there's no need to take copies of everything.  This makes the
                # process substantially quicker, but could produce
                # difficult-to-debug bugs if done without care, hence not being
                # the default.
                self.primes = seed.primes
                self.composites = seed.composites
            self._generator = chain(self.primes, self._prime_generator())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)

    def _prime_generator(self):
        if self.primes == []:
            yield 2
            self.primes.append(2)
            start = 3
        elif self.primes == [2]:
            start = 3
        else:
            start = self.primes[-1] + 2

        # This function is an implementation of an incremental Sieve of
        # Eratosthenes, based broadly on the algorithm by Richard Bird, as
        # described in O'Neill, Milssa E, "The Genuine Sieve of Eratosthenes",
        # <http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf>, accessed 21
        # August 2015, and apparently published in the Journal of Functional
        # Programming (2009) 19, pp 95-106, doi: 10.1017/S0956796808007004.
        for x in count(start, step=2):
            if x in self.composites:
                gens = self.composites.pop(x)
                for gen in gens:
                    self.composites[next(gen)].append(gen)
            else:
                # We're avoiding even numbers in this sieve entirely.  Since
                # this prime will clearly be odd, the generator increments by
                # double the prime each time, guaranteeing the next number will
                # always be odd too.  The starting point is thus triple the
                # prime, since we can do the first incremen immediately.
                gen = count(x * 3, x * 2)
                self.composites[next(gen)].append(gen)
                self.primes.append(x)
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
