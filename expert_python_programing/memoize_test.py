#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Created: 2014-08-03

# memoize test
# copied from Expert Python Programing p.367

cache = {}

def factorial(n):
    r = 1
    while n:
        r *= n
        n -= 1
    return r

def get_key(function, *args, **kw):
    key = '%s.%s:' % (function.__module__, function.__name__)
    hash_args = [str(arg) for arg in args]
    hash_kw = ['%s:%s' % (k, hash(v)) for k, v in kw.items()]
    return '%s::%s::%s' % (key, hash_args, hash_kw)

def memoize(get_key=get_key, cache=cache):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = get_key(function, *args, **kw)
            try:
                return cache[key]
            except KeyError:
                value = cache[key] = function(*args, **kw)
                return value
        return __memoize
    return _memoize

if __name__ == "__main__":
    cached_factorial = memoize()(factorial)
    cache.clear()
    print cached_factorial(10, test="TEST")
    print cache
