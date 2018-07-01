# -*- Coding: utf-8 -*-

""" Retain parameter data.

Currently, this module only use with sqlite.
"""

import os
import sqlite3


class Retainer(object):

    def __init__(self):
        # Temporary script.
        conn_dir = os.path.abspath(os.path.dirname(__file__))
        sqlite_relative_path = 'storage/sqlite/api.db'
        sqlite_path = os.path.join(conn_dir.replace('/pickup', ''),
                                   sqlite_relative_path)
        print sqlite_path
        # <-------
        self.conn = sqlite3.connect(sqlite_path)
        self.cur = self.conn.cursor()

    def insert(self, name, parameters):
        if not self.__has_database(name):
            self.__create_database(name)
            print 'Create database:{0}'.format(name)
        insert_sql = """INSERT INTO {0}(request) VALUES('{1}');"""
        for p in parameters:
            # Need url encode??
            self.cur.execute(insert_sql.format(name, p))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __has_database(self, name):
        self.cur.execute(
            """select count(*)
               from sqlite_master
               where type='table' and name='{0}'""".format(name)
            )
        has_table = self.cur.fetchone()[0]
        return has_table

    def __create_database(self, name):
        create_sql = \
            """
            CREATE TABLE {0}(request text default '',
                                response text default '',
                                velocity integer default 0
                                );
            """.format(name)
        index_sqls = [
            "CREATE INDEX {0}_request ON {0} (request);".format(name),
            "CREATE INDEX {0}_velocity ON {0} (velocity);".format(name)
            ]
        self.cur.execute(create_sql)
        for s in index_sqls:
            self.cur.execute(s)


if __name__ == '__main__':
    r = Retainer()
