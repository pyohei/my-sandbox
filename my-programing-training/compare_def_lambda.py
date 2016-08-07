#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Execution time comparision with "function" and "lambda".

Created: 2014-08-27
"""

def func_(x):
    if x % 2 == 0:
        return x ** 1000
    return x ** 500

lam_ = lambda x: x ** 1000 if x % 2 == 0 else x ** 500

if __name__ == "__main__":
    from timeit import timeit
    print "----- function -----"
    print timeit("[func_(x) for x in xrange(1,1000)]",
        setup="from __main__ import func_",
        number=1000)
    print "----- lambda -----"
    print timeit("[lam_(x) for x in xrange(1,1000)]",
        setup="from __main__ import lam_",
        number=1000)
    print "----- lambda -----"
    print timeit("[lam_(x) for x in xrange(1,1000)]",
        setup="from __main__ import lam_",
        number=1000)
    print "----- function -----"
    print timeit("[func_(x) for x in xrange(1,1000)]",
        setup="from __main__ import func_",
        number=1000)
