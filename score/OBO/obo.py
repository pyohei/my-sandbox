#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" OBO score calculation.

"""
import MySQLdb
import config as conf
from lib.db.dbConnector import MySqlConnection

class Calculation(object):

    def __init__(self, score):
        self.score = score

    def main(self):
        score = self.score
        print score
        return score

class Registration(object):

    def __init__(self, judging):
        """ init

        if possible, I call db connection from other module.
        """
        self.__connect()
        self.judging = judging
        self.contest_no = judging.contest_no
        self.player_no = judging.player_no
        self.judge_user = judging.judge_no
        self.scores = judging.scores

    def __connect(self):
        db = conf.CONNECTION["OBO"]
        self.conn = MySqlConnection(
            db["HOST"], db["DB"], db["USER"], db["PASSWD"])

    def main(self):
        for skating_no, score in enumerate(self.scores):
            self.__append_score(skating_no, score)

    def __append_score(self, skating_no, score):
        sql = (
            "insert into obo_score( "
            "    contest_no, "
            "    skating_no, "
            "    player_no, "
            "    judge_user, "
            "    technical_merit, "
            "    presentation "
            ") "
            "values ( "
            "    %s, "
            "    %s, "
            "    %s, "
            "    %s, "
            "    %s, "
            "    %s "
            "    ); " % (
                self.contest_no,
                skating_no + 1,
                self.player_no,
                self.judge_user,
                score.technicalmerit,
                score.presentation
                )
            )
        self.conn.insertRecord(sql)
