#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Contest Selector

Load contest lis by judging
"""

from lib.record import recordFactory


class Selector(object):

    def __init__(self, way=None, sort=None):
        if not way:
            way = "all"
        self.way = way
        self.sort = sort
        self.connection = recordFactory.init().get_connection()

    def select(self):
        exec("from %s import Selector" % (self.way))
        selector = Selector(self.connection, self.sort)
        recs = selector.select()
        return recs

if __name__ == "__main__":
    s = Selector()
    recs = s.select()
    for rec in recs:
        print rec
