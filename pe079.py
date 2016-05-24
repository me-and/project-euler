#!/usr/bin/env python3
'''
Passcode derivation

A common security method used for online banking is to ask the user for three
random characters from a passcode.  For example, if the passcode was 531278,
they may ask for the 2nd, 3rd and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.
'''

import os.path

HINT_PATH = os.path.join('pe079', 'keylog.txt')


def load_hints():
    with open(HINT_PATH) as hint_file:
        return set(line.strip() for line in hint_file)


# Start with the assumption that every digit only appears once.  This turns out
# to be true, and makes the solution considerably easier to find.  Without this
# assumption, we wouldn't be able to assert that, for example, there will be a
# character that needs no other characters to come after it.
if __name__ == '__main__':
    hints = load_hints()
    preceeding_characters = {c: set() for c in ''.join(hints)}

    # Create a map from each possible character to the characters that need to
    # come before it.
    for hint in hints:
        preceeding_characters[hint[2]].add(hint[0])
        preceeding_characters[hint[2]].add(hint[1])
        preceeding_characters[hint[1]].add(hint[0])

    # Start with an empty string, and while there are still characters to add,
    # add the first character we find which has all the necessary preceeding
    # characters already in the string.
    string = ''
    while preceeding_characters:
        character = next(c for c in preceeding_characters
                         if set(string) >= preceeding_characters[c])
        string += character
        del(preceeding_characters[character])

    print(string)
