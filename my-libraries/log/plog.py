#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Log Generator

This module is to meke log easily.
CREATED: 2014/7/22
"""

from datetime import datetime
import os



def start(message=""):
    if message:
        log.start(message)
    else:
        log.start()

def write(message):
    log.write(message)

def finish(message=""):
    if message:
        log.start(message)
    else:
        log.finish()

class Log:

    def __init__(self):
        self.LOG_DIR = "./log"
        self.LOG_NAME = "%s.log" % (datetime.now().strftime("%Y%m%d"))
        self.LOG_OBJ = None

    def set_log_dir(self, dir):
        self.LOG_DIR = dir

    def set_log_name(self, name):
        self.LOG_NAME = name

    def start(self, message="START"):
        if not os.path.exists(self.LOG_DIR):
            os.mkdir(self.LOG_DIR)
        LOG_PATH = os.path.join(self.LOG_DIR, self.LOG_NAME)
        if not os.path.exists(LOG_PATH):
            self.LOG_OBJ = open(LOG_PATH, "w")
        else:
            self.LOG_OBJ = open(LOG_PATH, "a")
        self.write("\n", direct=True)
        self.write(message)

    def finish(self, message="END"):
        self.write(message)
        self.LOG_OBJ.close()

    def write(self, message, direct=False):
        if direct:
            self.LOG_OBJ.write(message)
            return
        log_time = self.__watch_time()
        self.LOG_OBJ.write("\n%s..%s" % (log_time, message))

    def __watch_time(self, format=""):
        return datetime.now().strftime("%Y%m%d%H%M%S")

log = Log()

if __name__ == "__main__":
    start()
    write("test")
    finish()
