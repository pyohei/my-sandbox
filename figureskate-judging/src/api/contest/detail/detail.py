#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Handle contest details

This module have detail informations.
Mainly, execute for detail loader.

"""

from lib.db.dbConnector import MySqlConnection
import config as conf


def init():
    global __detail_instance
    if __detail_instance:
        return __detail_instance
    __detail_instance = Movie()
    return __detail_instance


class Detail(object):

    def __init__(self):
        self.__connect()
        self.contest_no = 0

    def _clear(self):
        self.contest_no = 0

    def __connect(self):
        db = conf.CONNECTION["OBO"]
        self.conn = MySqlConnection(
            db["HOST"], db["DB"], db["USER"], db["PASSWD"])

    def load(self, contest_no):
        sql = (
            "select * "
            "from contest_master m "
            "inner join contest_movie v "
            "on m.contest_no = v.contest_no "
            "where m.contest_no = %s "
            "; " % (
                contest_no
                )
            )
        return self.conn.fetchRecords(sql)
