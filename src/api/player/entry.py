#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Entry player infomation

"""
import MySQLdb
import config as conf
from lib.db.dbConnector import MySqlConnection

class Entry(object):

    def __init__(self, player):
        """ init

        if possible, I call db connection from other module.
       """
        self.__connect()
        self.player = player

    def __connect(self):
        db = conf.CONNECTION["OBO"]
        self.conn = MySqlConnection(
            db["HOST"], db["DB"], db["USER"], db["PASSWD"])

    def register(self):
        self.__append_score()

    def __append_score(self):
        sql = (
            "insert into player_master( "
            "player_name, "
            "player_nickname, "
            "degree, "
            "country "
            ") "
            "values ( "
            "    '%s', "
            "    '%s', "
            "    %s, "
            "    %s "
            "); " % (
                self.player["player_name"],
                self.player["player_nickname"],
                self.player["degree"],
                self.player["country"]
                )
            )
        print sql
        self.conn.insertRecord(sql)
