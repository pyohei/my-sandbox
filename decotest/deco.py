#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from functools import wraps

def decodef(**names):
    def deco(func):
        @wraps(func)
        def inner(self):
            print names
            return func(self)
        return inner
    return deco

def check(name):
    dic = {
        "apple": "red",
        "orange": "orange",
        "banana": "yellow"
        }
    return dic[name]
