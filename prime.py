'''Functions for working with primes.'''

from collections import defaultdict
from itertools import count

from sequence import MonatonicIncreasingSequence


class PrimeGenerator(MonatonicIncreasingSequence):
    '''Generate primes reasonably efficiently.'''
    def __init__(self):
        super().__init__(self._prime_generator())

    @staticmethod
    def _prime_generator():
        composites = defaultdict(list)

        yield 2

        # This function is an implementation of an incremental Sieve of
        # Eratosthenes, based broadly on the algorithm by Richard Bird, as
        # described in O'Neill, Milssa E, "The Genuine Sieve of Eratosthenes",
        # <http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf>, accessed 21
        # August 2015, and apparently published in the Journal of Functional
        # Programming (2009) 19, pp 95-106, doi: 10.1017/S0956796808007004.
        for x in count(3, step=2):
            if x in composites:
                gens = composites.pop(x)
                for gen in gens:
                    composites[next(gen)].append(gen)
            else:
                # We're avoiding even numbers in this sieve entirely.  Since
                # this prime will clearly be odd, the generator increments by
                # double the prime each time, guaranteeing the next number will
                # always be odd too.  The starting point is thus triple the
                # prime, since we can do the first increment immediately.
                gen = count(x * 3, x * 2)
                composites[next(gen)].append(gen)
                yield x

    def prime_factors(self, n):
        factors = defaultdict(int)
        for p in self:
            while n % p == 0:
                factors[p] += 1
                n //= p
            if p ** 2 > n:
                if n != 1:  # Happens if the original n was prime
                    factors[n] += 1
                return factors


# Global to use for the majority of functions, to avoid needing to recalculate
# values whenever the function is called.
primes = PrimeGenerator()

# Provide module-level functions based on the global PrimeGenerator instance.
prime_factors = primes.prime_factors
