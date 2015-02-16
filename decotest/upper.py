#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import deco
from base import Base

class Upper(Base):

    @deco.decodef(
        a="edit",
        b="list")
    def execute(self):
        print "execution!"
        return 10


class Tmp:

    def __init__(self):
        self.num = 1

    def main(self):
        u = Upper()
        print self.num + u.execute()


if __name__ == "__main__":
    t = Tmp()
    t.main()

