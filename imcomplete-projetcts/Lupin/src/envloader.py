"""Environ loader"""

import os


ENV_PREFIX = "LUPIN_ENV"


def load(PREFIX=None):
    """Load os envirion variables."""
    if PREFIX:
        ENV_PREFIX = PREFIX
    e = _Environ()
    for k, v in os.environ.items():
        if k.startswith(ENV_PREFIX):
            print 'ok {0}'.format(k)
            e.add(k, v)
    return e


class _Environ(object):
    """Environment class"""

    def add(self, k, v):
        """Add key and value."""
        self.__dict__[k] = v

    def to_dict(self):
        """Convert to instance variables to dictionary."""
        return self.__dict__

if __name__ == '__main__':
    l = load(PREFIX='H')
    print l.HOME
    print l.to_dict()
