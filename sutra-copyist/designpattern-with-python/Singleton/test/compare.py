#!/usr/local/bin/python
# -*- coding: utf-8 -*-

###### Singleton effect measure #######
# This module compares between Singleton and non-Singleton.


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            orig = SimpleCalc()
            cls._instance = orig
        return cls._instance


class nonSingleton(object):
    def __new__(cls):
        orig = SimpleCalc()
        cls._instance = orig
        return cls._instance


class SimpleCalc:
    def __init__(self):
        a = 0
        for b in range(0,100000000):
            a += b

if __name__ == "__main__":
    from datetime import datetime as ft
    output = open("./%s.log"%(ft.today().strftime("%Y%m%d%H%M%S")), "w")
    output.write("#####start####\n")
    import time
    output.write("\n---non-singleton---\n")
    for a in range(1, 6):
        s = time.time()
        nsingle = nonSingleton()
        output.write("%s time: %s sec.\n"%(a,time.time() - s))
    output.write("---singleton---\n")
    for a in range(1, 6):
        s = time.time()
        single = Singleton()
        output.write("%s time: %s sec.\n"%(a,time.time() - s))
    output.write("---singleton---\n")
    for a in range(1, 6):
        s = time.time()
        single = Singleton()
        output.write("%s time: %s sec.\n"%(a,time.time() - s))
    output.write("\n---non-singleton---\n")
    for a in range(1, 6):
        s = time.time()
        nsingle = nonSingleton()
        output.write("%s time: %s sec.\n"%(a,time.time() - s))
    output.write("\n####end####")
