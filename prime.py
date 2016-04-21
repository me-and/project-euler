'''Functions for working with primes.'''

from collections import defaultdict
from itertools import count


class OrderedSet(object):
    '''A limited object that acts like both a set and a list.'''
    # Could inherit from collections.abc objects or use one of the available
    # recipes for doing this, but I only require a very limited interface, so
    # I'm keeping it simple.
    def __init__(self, iterable=()):
        self._list = list(iterable)
        self._set = set(self._list)  # Don't assume we can iterate twice

    def add(self, value):
        self._list.append(value)
        self._set.add(value)

    def __contains__(self, value):
        return value in self._set

    def __iter__(self):
        return iter(self._list)

    def __getitem__(self, key):
        return self._list[key]

    def __len__(self):
        return len(self._list)


class PrimeGenerator(object):
    '''Generate primes reasonably efficiently.'''
    def __init__(self):
        self.primes = OrderedSet()
        self.composites = defaultdict(list)
        self._generator = self._prime_generator()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)

    def _prime_generator(self):
        self.primes.add(2)
        yield 2

        # This function is an implementation of an incremental Sieve of
        # Eratosthenes, based broadly on the algorithm by Richard Bird, as
        # described in O'Neill, Milssa E, "The Genuine Sieve of Eratosthenes",
        # <http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf>, accessed 21
        # August 2015, and apparently published in the Journal of Functional
        # Programming (2009) 19, pp 95-106, doi: 10.1017/S0956796808007004.
        for x in count(3, step=2):
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
                self.primes.add(x)
                yield x


# Global to use for the majority of functions, to avoid needing to recalculate
# values whenever the function is called.
_prime_generator = PrimeGenerator()


def prime_generator():
    '''Generate primes, using pre-generated ones if they exist.

    This copes just fine with having multiple instances of the generator in
    use, but it isn't thread safe.
    '''
    idx = 0
    while True:
        try:
            prime = _prime_generator.primes[idx]
        except IndexError:  # Haven't generated the next prime yet
            prime = next(_prime_generator)
        yield prime
        idx += 1


def prime_factors(n):
    factors = defaultdict(int)
    for p in prime_generator():
        while n % p == 0:
            factors[p] += 1
            n //= p
        if p ** 2 > n:
            if n != 1:  # Happens if the original n was prime
                factors[n] += 1
            return factors


def is_prime(n):
    if not _prime_generator.primes or n > _prime_generator.primes[-1]:
        # We haven't generated primes up to this number yet, so keep generating
        # them until we have.
        for x in _prime_generator:
            if n == x:  # Generated n as a prime
                return True
            elif n < x:  # Passed n without generating it
                return False
    else:
        return n in _prime_generator.primes
