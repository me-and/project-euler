#!/usr/bin/env python3
'''
Poker hands

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

- High Card: Highest value card.
- One Pair: Two cards of the same value.
- Two Pairs: Two different pairs.
- Three of a Kind: Three cards of the same value.
- Straight: All cards are consecutive values.
- Flush: All cards of the same suit.
- Full House: Three of a kind and a pair.
- Four of a Kind: Four cards of the same value.
- Straight Flush: All cards are consecutive values of same suit.
- Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen,
King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand  Player 1           Player 2             Winner
1     5H 5C 6S 7S KD     2C 3S 8S 8D TD       Player 2
      Pair of Fives      Pair of Eights
2     5D 8C 9S JS AC     2C 5C 7D 8S QH       Player 1
      Highest card Ace   Highest card Queen
3     2D 9C AS AH AC     3D 6D 7D TD QD       Player 2
      Three Aces         Flush with Diamonds
4     4D 6S 9H QH QC     3D 6D 7H QD QS       Player 1
      Pair of Queens     Pair of Queens
      Highest card Nine  Highest card Seven
5     2H 2D 4C 4D 4S     3C 3D 3S 9S 9D       Player 1
      Full House         Full House
      With Three Fours   With Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
'''

from functools import total_ordering
import os.path

RANKS = tuple('23456789TJQKA')


@total_ordering
class Card(object):
    cards = {}

    def __new__(cls, string):
        # Re-use existing card instances if they've already been created.
        try:
            return cls.cards[string]
        except KeyError:
            card = super().__new__(cls)
            cls.cards[string] = card
            return card

    def __init__(self, string):
        self.rank = string[0]
        self.suit = string[1]

    def __eq__(self, other):
        return self.rank == other.rank

    def __le__(self, other):
        return RANKS.index(self.rank) <= RANKS.index(other.rank)

    def __repr__(self):
        return "{}('{}{}')".format(self.__class__.__name__,
                                   self.rank, self.suit)

    def __str__(self):
        return '{}{}'.format(self.rank, self.suit)


@total_ordering
class Hand(object):
    def __init__(self, string):
        self.cards = tuple(map(Card, string.split()))

    def is_flush(self):
        return (self.cards[0].suit == self.cards[1].suit ==
                self.cards[2].suit == self.cards[3].suit == self.cards[4].suit)

    def is_straight(self):
        # Is a straight if the minimum rank is four below the maximum rank, and
        # each rank in between is represented.
        ranks = set(map(lambda c: RANKS.index(c.rank), self.cards))
        return max(ranks) - min(ranks) == 4 and len(ranks) == 5

    def group_cards_by_rank(self):
        ranks = {}
        for card in self.cards:
            ranks.setdefault(card.rank, []).append(card)
        return ranks

    def _score(self):
        # Provide a score from 1-9 for easy comparison between the different
        # hand types, then a list of cards to compare to determine the winner
        # if comparing hands of the same type (e.g. between two four-of-a-kind
        # hands).
        ranked = self.group_cards_by_rank()
        rank_groups = sorted([len(l) for l in ranked.values()])
        flush = self.is_flush()
        straight = self.is_straight()

        if straight and flush:
            # Straight (possibly royal) flush.  Compare high card.
            return 9, max(self.cards)
        elif rank_groups == [1, 4]:
            # Four of a kind.  Compare one of the cards in the four; because
            # there are four cards of the same rank there can never be a tie,
            # at least without playing with two decks.
            return 8, next(l for l in ranked.values() if len(l) == 4)[0]
        elif rank_groups == [2, 3]:
            # Full house.  Compare one of the cards in the three; as with
            # four-of-a-kind, that will always be sufficient.
            return 7, next(l for l in ranked.values() if len(l) == 3)[0]
        elif flush:
            # Flush.  Compare all the cards in the flush, in order from highest
            # to lowest.
            return 6, sorted(self.cards, reverse=True)
        elif straight:
            # Straight.  Compare the high card.
            return 5, max(self.cards)
        elif rank_groups == [1, 1, 3]:
            # Three of a kind.  Compare one card in the three, as for a full
            # house.
            return 4, next(l for l in ranked.values() if len(l) == 3)[0]
        elif rank_groups == [1, 2, 2]:
            # Two pairs.  Compare one card in the top pair, one card in the
            # lower pair, then the kicker.
            return 3, (sorted((l[0] for l in ranked.values() if len(l) == 2),
                              reverse=True) +
                       [next(l for l in ranked.values() if len(l) == 1)[0]])
        elif rank_groups == [1, 1, 1, 2]:
            # One pair.  Compare one card in the pair, then the kickers in
            # order.
            return 2, ([next(l for l in ranked.values() if len(l) == 2)[0]] +
                       sorted((l[0] for l in ranked.values() if len(l) == 1),
                              reverse=True))
        else:
            # High card.  Compare the cards in order.
            return 1, sorted(self.cards, reverse=True)

    def __eq__(self, other):
        return self._score() == other._score()

    def __lt__(self, other):
        s_score, s_tiebreak = self._score()
        o_score, o_tiebreak = other._score()
        if s_score == o_score:
            for s_t, o_t in zip(s_tiebreak, o_tiebreak):
                if s_t == o_t:
                    continue
                else:
                    return s_t < o_t
            # Equal
            return False
        else:
            return s_score < o_score

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__,
                                 ' '.join(str(card) for card in self.cards))


if __name__ == '__main__':
    with open(os.path.join('pe054', 'poker.txt')) as hand_file:
        print(sum(Hand(line[:14]) > Hand(line[15:29]) for line in hand_file))
