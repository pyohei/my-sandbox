#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import sys

"""
operation system manager
"""

def pwd():
    return os.getcwd()

def get_pid():
    return os.fork()

if __name__ == '__main__':
    print pwd()
    p = get_pid()

    if p > 0:
        print "pid:%s" % p
        sys.exit(0)
