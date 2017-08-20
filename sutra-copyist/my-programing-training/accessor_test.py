#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Created: 2014/10/25
# coding test of accessor method.

class Accessor:
    def __init__(self):
        self.x = None

    def getx(self):
        return self.x

    def setx(self, value):
        print self.x
        self.x = value

    def delx(self):
        del self.x

    x = property(getx, setx, delx)

def Property(func):
    return property(**func())

class decoAccessor:
    def __init__(self):
        self.x = None
        print "here"

    @Property
    def x():
        def fget(self):
            return self.x

        def fset(self, value):
            self.x = value

        return locals()

if __name__ == "__main__":
    """
    a = Accessor()
    a.x = 10
    print a.x
    # うーん。これだとset, get の定義がすべて必要なのか。。
    b = Accessor()
    b.y = 10
    print b.y
    # これはエラーでは
    # 追記：そんなことなかった。。
    b.test = "test"
    print b.test
    # もういっちょやってみる
    # できたではないか。。
    """
    a = decoAccessor()
    a.hoge = "hoge"
    a.foo = "foo"
    a.test = "ppp"
    print a.hoge
    print a.foo
    print a.test
    print "----"
    a = Accessor()
    a.hoge = "hogehoge"
    print a.hoge
