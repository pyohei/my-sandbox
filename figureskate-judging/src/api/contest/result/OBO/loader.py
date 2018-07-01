#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Loader OBO contest result

"""

from lib.record import recordFactory


class Loader(object):

    def __init__(self, contest_no):
        self.contest_no = contest_no
        self.conn = recordFactory.init().get_connection()

    def load(self):
        conn = self.conn
        conn.set_table("obo_score")
        conn.set_equal("contest_no", self.contest_no)
        recs = conn.select()
        return recs

if __name__ == "__main__":
    l = Loader(2)
    r = l.load()
