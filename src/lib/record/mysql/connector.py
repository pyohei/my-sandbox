#!/usr/local/bin/python
#-*- coding: utf-8 -*-

""" connecotr with mysql connection

"""

from controller import Controller

class Connectotr(object):

    def __init__(self, conn):
        self.conn = conn

    def get_connection(self):
        return Controller(self.conn)
