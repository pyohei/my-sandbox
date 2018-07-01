#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Templeta of database connection

Database connection base class.
First created in 2013/12/22
"""

from MySQLdb import connect, cursors


class MySqlConnection:

    """ Base class

    __init__:       connect database
    insertRecord:   insert records
    fetchRecords:   select records
    updateRecords:  update records
    deleteRecords:  delete records
    """

    def __init__(self, host, db, user, passwd, charset="utf-8"):
        self.conn = connect(
            host=host,
            db=db,
            user=user,
            passwd=passwd)
#            charset = charset)
#        self.conn = connect(host,db,user,passwd)
        self.cur = self.conn.cursor(cursors.DictCursor)
        self.cur.execute("SET NAMES utf8")

    def insertRecord(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def fetchRecords(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def updateRecords(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def deleteRecords(self, sql):
        self.execute(sql)
        self.conn.commit()

if __name__ == '__main__':
    pass
