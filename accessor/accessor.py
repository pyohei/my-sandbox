#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Acccessor tool.
But I cannt understand this module component
I wannt to use this without shadowing

*** about property ***
property(get type method,
         set type method,
         del type method)

"""

class Accessor(object):
    """ explanation is same as OldAccessor.
        the most important thing to progress property method,
        providing method to throw property method."""

    def __init__(self):
        self._x = None

    @property
    def x(self):
        pass
        #return self._x

    @x.setter
    def x(self, value):
        pass
        #self._x = value

    @x.deleter
    def x(self):
        pass
        #del self._x

class OldAccessor(object):
    """ this doesn't advanse decorator.
        You understand how to use in this way.
        process is only disuse
        (so, I get out comment each processes)"""

    def __init__(self):
        self._x = None

    def getter(self):
        pass
        #return self._x

    def setter(self, value):
        pass
        #self._x = value

    def deller(self):
        pass
        #print "deleting..."
        #del self._x

    x = property(getter, setter, deller)

# execute from console
if __name__ == '__main__':
    print "--- accessor test ---"
    a = Accessor()
    a.hoge = "hoge"
    print a.hoge
    del a.hoge
    try:
        print a.hoge
    except:
        print "nothing"
    o = OldAccessor()
    o.foo = "foo"
    print o.foo
    del o.foo
    try:
        print o.foo
    except:
        print "nothing2"
