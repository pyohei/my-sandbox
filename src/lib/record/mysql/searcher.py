#!/usr/local/bin/python
#-*- coding: utf-8 -*-

""" Search connection and tables.

Get all tables from defined database(config).
"""

from controller import Controller
from connector import Connectotr

class Searcher(object):

    def __init__(self, conn):
        """ ./loader.py read 'tables' and 'instance' directory.
        This is my first trial.
        """
        self.conn = conn
        self.tables = []
        self.instance = None

    def search(self):
        self.connection = Connectotr(self.conn)
        controller = Controller(self.conn)
        self.tables = self.__process(controller.get_tables())

    def __process(self, recs):
        """ process record. """
        tables = []
        for rec in recs:
            tables.extend(rec.values())
        return tables

if __name__ == "__main__":
    pass
