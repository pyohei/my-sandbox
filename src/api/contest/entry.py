#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Entry contest infomation

"""
import MySQLdb
import config as conf
from lib.db.dbConnector import MySqlConnection

class Entry(object):

    def __init__(self, contest):
        """ init

        if possible, I call db connection from other module.
        """
        self.__connect()
        self.contest = contest

    def __connect(self):
        db = conf.CONNECTION["OBO"]
        self.conn = MySqlConnection(
            db["HOST"], db["DB"], db["USER"], db["PASSWD"])

    def register(self):
        self.__append_score()

    def __append_score(self):
        sql = (
            "insert into contest_master( "
            "    contest_name, "
            "    contest_type, "
            "    judge_type, "
            "    contest_date "
            ") "
            "values ( "
            "    '%s', "
            "    %s, "
            "    %s, "
            "    '%s' "
            "    ); " % (
                self.contest["contest_name"],
                self.contest["contest_type"],
                self.contest["judge_type"],
                self.contest["contest_date"]
                )
            )
        print sql
        self.conn.insertRecord(sql)
