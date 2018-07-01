#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Contest All Selector

Select Contest from all valid contest
"""


class Selector(object):

    def __init__(self, connection, sort=None):
        self.sort = sort
        self.connection = connection

    def select(self):
        conn = self.connection
        conn.set_table("contest_master")
        conn.set_equal("invalid", 0)
        return conn.select()
