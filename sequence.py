import collections.abc as abc
from itertools import count


class OrderedSet(abc.MutableSequence):
    '''A list, but with fast container tests.'''
    def __init__(self, iterable=()):
        self._list = list(iterable)
        self._obj_counts = dict()
        for item in self._list:
            self._add_item_to_dict(item)

    def __getitem__(self, key):
        return self._list[key]

    def __setitem__(self, key, value):
        old_value = self._list[key]
        self._remove_item_from_dict(old_value)

        self._list[key] = value
        self._add_item_to_dict(value)

    def __delitem__(self, key):
        self._remove_item_from_dict(self._list[key])
        del self._list[key]

    def __len__(self):
        return len(self._list)

    def insert(self, index, value):
        self._add_item_to_dict(value)
        self._list.insert(index, value)

    def count(self, value):
        return self._obj_counts[value]

    def __contains__(self, key):
        return key in self._obj_counts

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self._list)

    def _add_item_to_dict(self, item):
        self._obj_counts[item] = self._obj_counts.get(item, 0) + 1

    def _remove_item_from_dict(self, item):
        if self._obj_counts[item] == 1:
            del self._obj_counts[item]
        else:
            self._obj_counts[item] -= 1


class MonatonicIncreasingSequence(abc.Container, abc.Iterable):
    def __init__(self, generator):
        self.history = OrderedSet()
        self.generator = self._generator(generator)

    def __iter__(self):
        return self._sequence()

    def _generator(self, generator):
        for value in generator:
            self.history.append(value)
            yield value

    def _sequence(self):
        '''Generate a new version of the sequence using the stored history.

        This will cope with multiple instances being in use, but it isn't
        thread safe.
        '''
        for idx in count():
            try:
                nxt = self.history[idx]
            except IndexError:  # Haven't generated this number yet
                nxt = next(self.generator)
            yield nxt

    def __contains__(self, number):
        if not self.history or number > self.history[-1]:
            # We haven't generated numbers up to the number under test yet, so
            # keep generating them until we have.  If we generate a number
            # equal to the number under test, we know it's in the sequence; if
            # we pass it, we know it isn't.
            return number == next(n for n in self.generator if n >= number)
        else:
            return number in self.history