#!/usr/bin/env python3
'''
Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''

from itertools import chain
import sys

from prime import primes, MillerRabinPrimes

miller_rabin = MillerRabinPrimes()

# Sketch solution:
#
# - Define D[p] to be the set of all primes less than a prime p which can be
#   concatenated on either side of p to produce a new prime.  For example, D[3]
#   is {}, D[7] is {3}, and D[19] is {7, 13}.
#
# - Use the dictionary above to recursively find a solution:
#
#   - Define two sets, P and Q.  All primes in P must be concatable with each
#     other to produce new primes.  All primes in Q must be concatable with all
#     primes in P to produce new primes, but not necessarily with each other.
#
#   - Initialize P to contain a single prime, p, and Q to contain D[p].
#
#   - Recurse by picking a prime, Q, in Q.  By definition, we can add q to P to
#     to obtain a new P' with the same property as the original P; to get the
#     new Q' we take the intersection of the original Q and D[q].

#   - If we obtain a set P that contains the desired number of primes, we have
#     a solution (although we have no guarantee it's the solution with the
#     minimal sum); if we obtain sets P and Q such that the total number of
#     elements in both sets is less than the desired number of primes, we know
#     we have no solution and can stop recursing.
#
# - At each point, we only need to know about D[p] for p less than whatever our
#   starting prime is, so we can just iterate over primes as we generate them.
#
# By example, looking for four primes with this property (where we know the
# solution is the one given in the problem description):
#
# - For primes p < 97, D[p] has at most two elements, so P and Q have at most
#   three elements in them so can never provide a solution.
#
# - For D[97] = {7, 19, 43}, so initialize P = {97}, Q = {7, 19, 43}.
#
# - Pick a prime in Q, say 43.  D[43] = {}, so adding 43 to P gives P = {43,
#   97} and Q = {}, so no solution.  D[19] = {7, 13} and D[7] = {3}, producing
#   Q' = {7} and Q' = {} respectively, so these too cannot give solutions.
#
# - Skipping intermediate steps until we get to 673, consider P = {673}, Q =
#   D[673] = {3, 7, 109, 199, 397, 457, 499, 613}.
#
# - Pick a prime in Q, say 499.  D[499] = {3, 43, 151, 181, 211, 229, 277,
#   349}, so P' = {499, 673}, Q' = {3}.  So this cannot be a solution.
#
# - Pick a different prime in Q, say 109.  D[109] = {3, 7}, so P' = {109, 673},
#   and Q' = {3, 7}.  This is still a potential solution, so recurse.
#
# - Pick 3 fom Q'.  D[3] = {}, so P'' = {3, 109, 673}, and Q'' = {}, so this
#   cannot be a solution.  Back up and pick a different prime from Q', 7, and
#   we get P'' = {7, 109, 673} and Q'' = {3}.  As a final step, pick 3 from Q'
#   to give P''' as {3, 7, 109, 673}, which is the solution we were looking
#   for.


def meets_concat_requirement(prime_one, prime_two):
    return (int(str(prime_one) + str(prime_two)) in miller_rabin and
            int(str(prime_two) + str(prime_one)) in miller_rabin)


def prime_pairs(prime):
    # Return the primes lower than the given prime that meet the concat
    # requirement.
    return {paired_prime for paired_prime in primes.range(prime - 1)
            if meets_concat_requirement(prime, paired_prime)}


def recurse(goal, s1, s2, pairs):
    if len(s1) == goal:  # Have a solution
        return [s1]
    if len(s1) + len(s2) < goal:  # No possible solutions
        return []

    solutions = []
    for prime in s2:
        solutions.extend(recurse(goal, s1 | {prime}, s2 & pairs[prime], pairs))
    return solutions

if __name__ == '__main__':
    try:
        goal = int(sys.argv[1])
    except IndexError:
        goal = 5

    pairs = {}
    answer = sys.maxsize  # Well above the actual result, so we can use `min`
    for prime in primes.range(3, None):
        if prime > answer:
            # This prime is greater than the best answer we have, so this prime
            # and higher primes cannot possibly produce a better answer.
            break
        pairs[prime] = prime_pairs(prime)
        results = recurse(goal, {prime}, pairs[prime], pairs)
        if results:
            # It turns out the first answer this algorithm produces is correct,
            # but it doesn't take very long to verify this, so we don't break
            # out of the loop until we're actually confident the answer is
            # right.
            answer = min([answer] + [sum(result) for result in results])

    print(answer)
