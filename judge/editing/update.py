#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Update judge profile

Update judge profile
"""

from lib.record import recordFactory
from datetime import datetime

COMP_ITEMS = ["judge_first_name", "judge_last_name", "judge_nickname",
    "judge_capacity", "email"]

class Update(object):

    def __init__(self, judge_no):
        self.judge_no = judge_no
        self.conn = recordFactory.init().get_connection()

    def update(self, profiles):
        cur_profile = self.__load_profile()[0]
        if self.__is_same(cur_profile, profiles):
            print "Same Data"
            return
        self.__update(profiles)

    def __load_profile(self):
        conn = self.conn
        conn.clear()
        conn.set_table("judge_master")
        conn.set_equal("judge_no", self.judge_no)
        return conn.select()

    def __is_same(self, cur, new):
        for i in COMP_ITEMS:
            if cur[i] != new[i]:
                return False
        return True

    def __update(self, profiles):
        conn = self.conn
        conn.clear()
        conn.set_table("judge_master")
        conn.set_equal("judge_no", self.judge_no)
        for key in COMP_ITEMS:
            conn.set_sets(("%s" % (key), profiles[key]))
        conn.set_sets(("update_user", str(self.judge_no)))
        conn.update()
        conn.clear()
