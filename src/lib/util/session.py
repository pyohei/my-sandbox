#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Session liblary

This module give about session.
"""

import random
import password
import MySQLdb
import config as conf
from datetime import datetime
from datetime import timedelta
from lib.db.dbConnector import MySqlConnection

__session_instance = None

def init():
    global __session_instance
    if __session_instance:
        return __session_instance
    __session_instance = Session()
    return __session_instance

class Session(object):

    def __init__(self):
        self.session_id = 0
        self.__connect()

    def has(self, session_id):
        sql = (
            "select session_no "
            "from session "
            "where session_id = '%s' "
            "  and limit_datetime > '%s' "
            "; " % (
                session_id,
                datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                )
            )
        print sql
        rec = self.conn.fetchRecords(sql)
        if rec:
            return True
        return False

    def publish(self, user):
        session_length = int(random.uniform(40, 50))
        session_id = password.generator(session_length)
        sql = ("insert into session( "
            "session_id, "
            "limit_datetime, "
            "judge_no "
            ") "
            "values ( "
            "'%s', "
            "'%s', "
            " %s "
            " ); " % (
                session_id,
                datetime.now() + timedelta(days=1),
                user["user_id"],
                )
            )
        print sql
        self.conn.insertRecord(sql)
        cookie = {}
        cookie["session_id"] = session_id
        cookie["judge_id"] = user["user_id"]
        cookie["expires"] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        return cookie

    def can_login(self, judge_no, passwd):
        hash_pass = password.encrypt(passwd)
        sql = (
            "select * "
            "from judge_password "
            "where judge_no = %s "
            "  and password = '%s' "
            " ; " % (
                judge_no,
                hash_pass)
            )
        rec = self.conn.fetchRecords(sql)
        if rec:
            return True
        return False

    def select_judge_no(self, session_id):
        sql = (
            "select judge_no "
            "from session "
            "where session_id = '%s' "
            "  and limit_datetime > '%s' "
            "; " % (
                session_id,
                datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                )
            )
        rec = self.conn.fetchRecords(sql)
        print rec
        if rec:
            return rec[0]["judge_no"]
        return None

    def __connect(self):
        db = conf.CONNECTION["OBO"]
        self.conn = MySqlConnection(
            db["HOST"], db["DB"], db["USER"], db["PASSWD"])

if __name__ == "__main__":
    s = Session("a", Db)
    s.has()
    s.new_setting()
