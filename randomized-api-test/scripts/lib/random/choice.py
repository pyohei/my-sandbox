# -*- Coding: utf-8 -*-

""" Randomize Choice

"""

import random


def pick_up(choices, exceptions=[]):
    targets = [c for c in choices if c not in exceptions]
    return random.choice(targets)


def rearrange(choices, size=None, complete=True):
    if not complete and size:
        raise KeyError('Do not use `size` when you do not use `complete`')
    random.shuffle(choices)
    if size:
        complete = False
    if complete:
        return choices
    if not size:
        size = random.randint(0, len(choices))
    return choices[0:size]


if __name__ == '__main__':
    print pick_up(['DC', 'AB'], ['AB'])
    print rearrange(['DM', 'MD', 'CD', 'DVD'])
    print rearrange(['DM', 'MD', 'CD', 'DVD'], size=2)
    print rearrange(['DM', 'MD', 'CD', 'DVD'], complete=False)
