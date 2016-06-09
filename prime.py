'''Functions for working with primes.'''

from collections import defaultdict
import collections.abc as abc
from itertools import count
from math import log
import random

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


class MillerRabinPrimes(abc.Container):

    # Limit for trial division established by experimentation with problem 60.
    def __init__(self,
                 deterministic=True,
                 witness_generator=None,
                 trial_division_limit=52):
        if witness_generator is None:
            if deterministic:
                self.generate_witnesses = self._deterministic_witnesses
            else:
                self.generate_witnesses = self._random_witnesses
        else:
            self.generate_witnesses = witness_generator

        self.low_prime_limit = trial_division_limit
        self.low_primes = set(primes.range(trial_division_limit))

    @staticmethod
    def _random_witnesses(possible_prime, num_witnesses=20):
        # Generate the requested number of witnesses randomly from the suitable
        # range, being [2, n-2] where n is the number being tested.
        return random.sample(range(2, possible_prime - 1),
                             min(num_witnesses, possible_prime - 3))

    @staticmethod
    def _deterministic_witnesses(possible_prime):
        # Below based on http://primes.utm.edu/prove/prove2_3.html
        if possible_prime < 2047:
            return (2,)
        if possible_prime < 1373653:
            return (2, 3)
        if possible_prime < 9080191:
            return (31, 73)
        if possible_prime < 25326001:
            return (2, 3, 5)
        if possible_prime < 4759123141:
            return (2, 7, 61)
        if possible_prime < 118670087467 and possible_prime != 3215031751:
            return (2, 3, 5, 7)
        if possible_prime < 2152302898747:
            return (2, 3, 5, 7, 11)
        if possible_prime < 3474749660383:
            return (2, 3, 5, 7, 11, 13)
        if possible_prime < 341550071728321:
            return (2, 3, 5, 7, 11, 13, 17)

        # Assume the generalized Riemann hypothesis holds for the below to be
        # deterministic for all possible primes.  Based on
        # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
        return range(2, 1 + min(possible_prime - 1,
                                int(2 * log(possible_prime) ** 2)))

    def __contains__(self, item):
        # Trial division suggested by http://primes.utm.edu/prove/prove2_3.html
        # and experimentation with problem 60 shows it does improve
        # performance.
        if item <= self.low_prime_limit:
            return item in self.low_primes
        for prime in self.low_primes:
            if item % prime == 0:
                return False

        # The below implements the Miller-Rabin primality test, based largerly
        # on the pseudocode example at
        # https://en.wikipedia.org/wiki/Miller–Rabin_primality_test.
        #
        # If this returns False, the number is definitely composite.  If this
        # returns True, then whether the number is definitely prime or merely
        # probably prime depends on whether the set of witnesses tested was
        # sufficient for the algorithm to be deterministic or not.
        d = item - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1

        for witness in self.generate_witnesses(item):
            if not self._single_prime_test(witness, d, r, item):
                return False

        return True

    @staticmethod
    def _single_prime_test(witness, d, r, item):
        x = pow(witness, d, item)
        if x == 1 or x == item - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, item)
            if x == 1:
                return False
            if x == item - 1:
                return True
        return False
