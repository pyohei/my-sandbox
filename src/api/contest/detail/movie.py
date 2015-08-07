#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Contest movie

Handle contest movie.
Give player_no, return movie url...
"""

from lib.db.dbConnector import MySqlConnection
import config as conf

__movie_instance = None


def init():
    global __movie_instance
    if __movie_instance:
        return __movie_instance
    __movie_instance = Movie()
    return __movie_instance


class Movie(object):

    def __init__(self):
        self.player_no = 0
        self.__connect()

    def __connect(self):
        db = conf.CONNECTION["OBO"]
        self.conn = MySqlConnection(
            db["HOST"], db["DB"], db["USER"], db["PASSWD"])

    def get_url(self, player_no):
        sql = (
            "select url "
            "from   contest_movie "
            "where  movie_no = '%s'; " % (
                player_no
                )
            )
        print sql
        return self.conn.fetchRecords(sql)[0]["url"]
