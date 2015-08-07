#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Create SQL and execute

"""

from datetime import datetime
from time import time
import config


class Creator:

    def __init__(self, conn):
        self.log_file_path = config.LOG_FILE
        self.conns = conn
        self.clear()

    def clear(self):
        self.connection = None
        self.database = None
        self.main_table = None
        self.columns = []
        self.sets = []
        self.where = []
        self.groupby = []
        self.insert_values = []
        self.limit = 0
        self.sql = ""

    def set_table(self, table):
        for name, conn in self.conns.items():
            if table in conn["tables"]:
                self.database = name
                self.main_table = table
                self.__connect()
                return
        raise ValueError(
            "No table detected. table name '%s' " % (
                table))

    def set_database(self, database):
        if self.database:
            raise ValueError(
                "Already setted database name.")
        self.database = database
        self.__connect()

    def set_columns(self, columns):
        self.columns = columns

    def set_equal(self, column, value, table=None, table_no=0):
        sql = "%s = %s" % (column, self.__check_str(value))
        self.where.append(sql)

    def set_in(self, column, values, table=None, table_no=0):
        value_format = [str(self.__check_str(v)) for v in values]
        sql = "%s in (%s)" % (column, ",".join(value_format))
        self.where.append(sql)

    def set_range(self, column, start=None, end=None):
        if start:
            sql = "%s >= %s" % (column, str(start))
            self.where.append(sql)
        if end:
            sql = "%s <= %s" % (column, str(end))
            self.where.append(sql)

    def set_sets(self, sets):
        if isinstance(sets, tuple):
            sets = [sets]
        self.sets += sets

    def set_insert_values(self, values, header=True):
        if not header:
            self.insert_values.append(" ")
        else:
            self.insert_values.append(
                "(" + ", ".join(
                    str(v) for v in values[0]) + ")")
        for vs in values[1:]:
            self.insert_values.append("(" + ", ".join(
                str(self.__check_str(v)) for v in vs) + ")")
        print self.insert_values

    def __check_str(self, string):
        if isinstance(string, str):
            return "'%s'" % (string)
        return string

    def __convert_int(self, num):
        try:
            return int(num)
        except:
            raise TypeError(
                "Error in convet number into 'int'. '%s'" % (num))

    def __connect(self):
        self.connection = self.conns[
            self.database][
            "connection"].get_connection()

    def select(self):
        sql = "select "
        if not self.columns:
            self.columns = ["*"]
        sql += "%s " % (",".join(self.columns))
        sql += "from %s " % (self.main_table)
        if self.where:
            sql += "where "
            sql += "%s " % (" and ".join(self.where))
        if self.limit:
            sql += "limit %s " % (str(self.limit))
        sql += ";"
        t = time()
        recs = self.connection.fetch(sql)
        self.logging_sql(sql, time() - t)
        return recs

    def insert(self):
        sql = "insert into %s " % (self.main_table)
        sql += self.insert_values[0]
        sql += " values "
        sql += ", ".join(self.insert_values[1:])
        sql += ";"
        t = time()
        self.connection.insert(sql)
        self.logging_sql(sql, time() - t)

    def update(self):
        sql = "update %s " % (self.main_table)
        sql += "set %s " % (", ".join(
            [k[0] + " = " + self.__check_str(k[1]) for k in self.sets]))
        if self.where:
            sql += "where "
            sql += "%s " % (" and ".join(self.where))
        sql += ";"
        t = time()
        self.connection.update(sql)
        self.logging_sql(sql, time() - t)

    def delete(self):
        sql = "delete from %s " % (self.main_table)
        if not self.where:
            raise EOFError(
                "You'll delete all table contents!"
                "Reconfirm your sql! table: %s" % (self.main_table))
        if self.where:
            sql += "where "
            sql += "%s " % (" and ".join(self.where))
        sql += ";"
        t = time()
        self.connection.delete(sql)
        self.logging_sql(sql, time() - t)

    # direct sql is for unsupport sql
    # and for transition period
    def direct_select(self, sql):
        return self.connection.fetch(sql)

    def direct_insert(self, sql):
        self.connection.insert(sql)

    def direct_update(self, sql):
        self.connection.update(sql)

    def direct_delete(self, sql):
        self.connection.delete(sql)

    def logging_sql(self, sql, time):
        now_time = datetime.now().strftime("%Y%m%d%H%M%S")
        f = open(self.log_file_path, "a")
        f.write("%s,%s,%s\n" % (now_time, sql, str(time)))
        f.close()
