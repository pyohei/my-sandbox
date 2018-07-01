#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" MySql Connection

Connect with MySQL.
Call directory, you can use mysql collenction
easilly.
(some day, I'll make mysql easy connector for
batch connection.)
"""

from loader import Loader
from query.creator import Creator

import config


class Connection(object):

    def __init__(self, connections=None):
        self.connection_maps = None
        self.connections = connections
        if not self.connections:
            self.connections = config.CONNECTIONS

    def connect(self):
        file_path = config.RECORD_CACHE
        loader = Loader(self.connections, file_path)
        self.connection_maps = loader.load()

    def get_connections(self):
        return Creator(self.connection_maps)

if __name__ == '__main__':
    c = Connection()
    c.connect()
    d = c.get_connections()
    print d
