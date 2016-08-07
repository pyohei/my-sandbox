#!/usr/local/bin/python
#-*- coding: utf-8 -*-

# Created: 2014-03-08


class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        print cls._state
        ob.__dict__ = cls._state
        return ob
       
class MyClass(Borg):
    a = 1

class MyClassRoom(Borg):
    b = 3



if __name__ == '__main__':
    one = MyClass()
    two = MyClass()
    print one.a
    two.a = 4
    print "------"
    print one.a
    third = MyClassRoom()
    print third.a
    print third.b
