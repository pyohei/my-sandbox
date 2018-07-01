#!/usr/local/bin/python
#-*- coding: utf-8 -*-

""" Record Factory

This module supplies record operation instance.
Indicate record type, you can get instance handling record.
Available way is below.
    - mysql

Instance getting from method 'get_connection()' can operate
record.

To understand the way of instance, look module 'Creator.py'
in using way directory.
"""

__RECORD_FACTORY = None
IMPORT_CODE = "from %s.connection import Connection as cls "

def init(way=None):
    global __RECORD_FACTORY
    if __RECORD_FACTORY:
        return __RECORD_FACTORY
    if way:
        __RECORD_FACTORY = RecordFactory(way)
    else:
        __RECORD_FACTORY = RecordFactory()
    return __RECORD_FACTORY

class RecordFactory(object):

    def __init__(self, way="mysql"):
        self.way = way
        self.conns = None
        self.__connect()

    def __connect(self):
        imp_code = IMPORT_CODE % (self.way)
        exec(imp_code)
        conn = cls()
        conn.connect()
        self.conns = conn.get_connections()

    def get_connection(self):
        return self.conns

if __name__ == '__main__':
    rf = RecordFactory()
    conn = rf.get_connection()
    conn.set_table("")
    conn.set_columns(["", ""])
    conn.set_equal("", 1)
    conn.set_in("", [1,2])
    conn.set_range("", 11, 16)
    print conn.select()
    conn.clear()
    conn.set_table("")
    conn.set_sets([("", "30")])
    conn.set_equal("", 1)
    conn.update()
    print "ok update"
    conn.clear()
    conn.set_table("")
    conn.set_equal("", "35")
    conn.delete()
    print "ok delete"
    conn.clear()
    conn.set_table("")
    conn.set_insert_values([("", "", "url"),
        (3, 0, "http://"), (4, 0, "http://")])
    conn.insert()
    print "ok_insert"
