#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Session liblary

This module give about session.
"""

#import passwd


class Session(object):

    def __init__(self, id):
        self.session_id = id
        self.session_class = cls()

    def has(self):
        return self.session_class.has_session(self.session_id)

    def new_setting(self):
        cls = self.session_class
        new_session = self.__create()
        cls.save()

    def __create(self):
        print "oooo"
        return
        return passwd.generator(50)

class Db(object):

    def __init__(self):
        pass

    def has_session(self):
        print "ok"

    def save(self):
        print "save"


class CVS(object):
    pass

if __name__ == "__main__":
    s = Session("a", Db)
    s.has()
    s.new_setting()
