#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Register of contest.

Register contest detail.

"""

from lib.record import recordFactory

class Register(object):

    def __init__(self):
        factory = recordFactory.init()
        self.conn = factory.get_connection()
        self.conn.clear()

    def register(self, form, contest_no):
        errs = []
        errs =  Checker(form).check()
        if errs:
            raise ValueError(
                "Input Value Error in contest register. %s" % (
                ",".join(errs))
                )
        form = self.__set_contest_no(form, contest_no)
        self.__register(form)

    def __register(self, form):
        conn = self.conn
        conn.clear()
        conn.set_table("contest_movie")
        conn.set_insert_values(self.__set_values(form))
        conn.insert()

    def __set_values(self, forms):
        v_sets = []
        keys = {
            "player_no": "player",
            "url": "movie_link",
            "contest_no": "contest_no",
            "start_time": "start_time",
            "end_time": "end_time"
            }
        v_sets.append(tuple(keys.keys()))
        for num, form in enumerate(forms):
            values = tuple([form[v+str(num+1)] for v in keys.values()])
            v_sets.append(values)
        return v_sets

    def __set_contest_no(self, forms, contest_no):
        f = []
        for num, form in enumerate(forms):
            key = "contest_no" + str(num + 1)
            form[key] = contest_no
            f.append(form)
        return f

class Checker(object):

    def __init__(self, form):
        self.form = form

    def check(self):
        return []
        pass
