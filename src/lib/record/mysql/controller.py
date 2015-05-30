#!/usr/local/bin/python
#-*- coding: utf-8 -*-

""" Controller of MySQLdb

"""

from MySQLdb import connect,cursors

class Controller():
    """ MySQLdb contoroller.

    *old method(basically, don't use)*
    __init__:       connect database
    insertRecord:   insert records
    fetchRecords:   select records
    updateRecords:  update records
    deleteRecords:  delete records


    """

    def __init__(self, connection):
        self.__check(connection.keys())
        self.database_name = connection["DB"]
        self.conn = connect(
            host = connection["HOST"],
            db = connection["DB"],
            user = connection["USER"],
            passwd = connection["PASSWD"])
        self.cur = self.conn.cursor(cursors.DictCursor)

    def insertRecord(self,sql):
        """ *old type* insert records """
        self.cur.execute(sql)
        self.conn.commit()


    def fetchRecords(self,sql):
        """ *old type* fetch records """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def updateRecords(self,sql):
        """ *old type* update records """
        self.cur.execute(sql)
        self.conn.commit()

    def deleteRecords(self,sql):
        """ *old type* delete records """
        self.execute(sql)
        self.conn.commit()

    def fetch(self,sql):
        """ fetch records"""
        self.cur.execute("SET NAMES utf8")
        self.cur.execute(sql)
        return self.cur.fetchall()

    def a_fetch(self,sql):
        """ fetch record(one record type dict)"""
        self.cur.execute("SET NAMES utf8")
        self.cur.execute(sql)
        return self.cur.fetchone()

    def insert(self,sql):
        self.__exec(sql)

    def update(self,sql):
        self.__exec(sql)

    def delete(self,sql):
        self.__exec(sql)

    def __exec(self, sql):
        """ change record process"""
        self.cur.execute("SET NAMES utf8")
        self.cur.execute(sql)
        self.conn.commit()

    def get_tables(self):
        """ get table list setted database """
        sql = "show tables from %s; " % (self.database_name)
        return self.fetch(sql)

    def get_databases(self):
        """ get databases from database server"""
        sql = "show database; "
        return self.fetch

    def __check(self, headers):
        """ check connection argment"""
        connection_names = ["HOST", "DB", "USER", "PASSWD"]
        invalid_names = [h for h in headers
            if h not in connection_names]
        if invalid_names:
            raise NameError(
                "Having valid keys in connection: %s" % (
                ",".join(invalid_names)))


if __name__ == '__main__':
    pass

