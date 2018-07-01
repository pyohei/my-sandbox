#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Entry player infomation

"""
import config as conf
from lib.db.dbConnector import MySqlConnection
from lib.util import password


class Entry(object):

    def __init__(self, judge):
        """ init

        if possible, I call db connection from other module.
        """
        self.__connect()
        self.judge = judge

    def __connect(self):
        db = conf.CONNECTION["OBO"]
        self.conn = MySqlConnection(
            db["HOST"], db["DB"], db["USER"], db["PASSWD"])

    def register(self):
        self.__append_score()
        hash_pass = password.encrypt(self.judge["password_master"])
        judge_no = self.__load_judge_no()
        print judge_no
        self.__append_password(judge_no, hash_pass)

    def __append_score(self):
        sql = (
            "insert into judge_master( "
            "    judge_first_name, "
            "    judge_last_name, "
            "    judge_nickname, "
            "    judge_capacity, "
            "    email, "
            "    register_time "
            ") "
            "values ( "
            "    '%s', "
            "    '%s', "
            "    '%s', "
            "    %s, "
            "    '%s', "
            "    '%s' "
            " ); " % (
                self.judge["judge_first_name"],
                self.judge["judge_last_name"],
                self.judge["judge_nickname"],
                self.judge["judge_capacity"],
                self.judge["email"],
                self.judge["register_time"]
                )
            )
        print sql
        self.conn.insertRecord(sql)

    def __append_password(self, judge_no, password):
        sql = (
            "insert into judge_password( "
            "   judge_no, "
            "   password "
            ") "
            "values( "
            "   %s, "
            "   '%s' "
            "); " % (
                judge_no,
                password
                )
            )
        print sql
        self.conn.insertRecord(sql)

    def __load_judge_no(self):
        sql = (
            "select judge_no "
            "from judge_master "
            "where email = '%s' "
            "; " % (
                self.judge["email"]
                )
            )
        print sql
        return self.conn.fetchRecords(sql)[0]["judge_no"]
