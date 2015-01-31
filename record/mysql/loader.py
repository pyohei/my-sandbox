#!/usr/local/bin/python
#-*- coding: utf-8 -*-

""" MySQL connection Loader.

Load MySQL connections.
Connection data have cache.

Load format:
    {"xxxx":
        {"tables": ["table1", "table2", ..... , "table30"],
         "connection": XXXXXXX
        },
    }
"""


import os
import pickle
from searcher import Searcher


class Loader(object):

    def __init__(self, connections, path):
        self.file_path = path
        self.connections = connections

    def load(self):
        if os.path.exists(self.file_path):
            f = open(self.file_path, "r")
            conn_map = pickle.load(f)
            f.close()
            return conn_map
        conn_maps = {}
        for name,conn in self.connections.items():
            conn_map = {}
            searcher = Searcher(conn)
            searcher.search()
            conn_map["tables"] = searcher.tables
            conn_map["connection"] = searcher.connection
            conn_maps[name] = conn_map
        f = open(self.file_path, "w")
        pickle.dump(conn_maps, f)
        f.close()
        return conn_maps

if __name__ == "__main__":
    pass
