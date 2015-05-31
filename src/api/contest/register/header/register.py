#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Register of contest.

Register contest detail.

"""

from lib.record import recordFactory

class Register(object):

    def __init__(self):
        self.contest_no = 0
        factory = recordFactory.init()
        self.conn = factory.get_connection()
        self.conn.clear()

    def register(self, form):
        errs = []
        errs =  Checker(form).check()
        if errs:
            raise ValueError(
                "Input Value Error in contest register. %s" % (
                ",".join(errs))
                )
        self.__register(form)
        self.__set_contest_no(form)

    def __register(self, form):
        conn = self.conn
        conn.set_table("contest_master")
        conn.set_insert_values(self.__set_values(form))
        conn.insert()

    def __set_values(self, form):
        v_sets = []
        keys = ("contest_name",
            "contest_type",
            "judge_type",
            "contest_date"
            )
        values = tuple([form[k] for k in keys])
        v_sets.append(keys)
        v_sets.append(values)
        return v_sets

    def get_contest_no(self):
        if not self.contest_no:
            raise ValueError(
                "not existing contest_no")
        return self.contest_no

    def __set_contest_no(self, form):
        conn = self.conn
        conn.set_table("contest_master")
        conn.set_equal("contest_name", form["contest_name"])
        rec = conn.select()
        self.contest_no = rec[0]["contest_no"]

class Checker(object):

    def __init__(self, form):
        self.form = form

    def check(self):
        return []

