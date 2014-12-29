#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Editing judge profile

Edit judge profile
"""

from lib.record import recordFactory

class Editing(object):

    def __init__(self, judge_no):
        self.judge_no = judge_no
        self.conn = recordFactory.init().get_connection()

    def load_profile(self):
        recs = self.__load_profile()
        print recs
        return recs

    def __load_profile(self):
        conn = self.conn
        conn.set_table("judge_master")
        conn.set_equal("judge_no", self.judge_no)
        return conn.select()
