#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Contest handler

This handle contest data.
"""

import config as conf
import os
import pickle

__handler_instance = None

"""
difinision 'init' may be bat.
because, in this instance is variable of value
"""
def init():
    global __handler_instance
    if __handler_instance:
        __handler_instance._clear()
        return __handler_instance
    __handler_instance = Handler()
    return __handler_instance

class Handler(object):

    def __init__(self):
        self._clear()

    def _clear(self):
        self.ins = None

    def has_judgeing_file(self, judge_no):
        file_name = "%s.pickle" % str(judge_no)
        file_path = conf.JUDGING_FILE_DIR + "/" + file_name
        return os.path.exists(file_path)

    def create_judging_file(self, judge_no, contest):
        print contest
        file_name = "%s.pickle" % judge_no
        file_path = conf.JUDGING_FILE_DIR + "/" + file_name
        with open("%s" % file_path, "w") as f:
            pickle.dump(contest, f)

    def load(self, judge_no):
        file_name = "%s.pickle" % judge_no
        file_path = conf.JUDGING_FILE_DIR + "/" + file_name
        with open(file_path, "r") as f:
            self.ins = pickle.load(f)
        if self.ins is None:
            raise ValueError, "no instance in file"
        #return self.ins

    def load_test(self, judge_no):
        file_name = "%s.pickle" % judge_no
        file_path = conf.JUDGING_FILE_DIR + "/" + file_name
        with open(file_path, "r") as f:
            self.ins = pickle.load(f)
        if self.ins is None:
            raise ValueError, "no instance in file"
        return self.ins

    def save(self):
        self.create_judging_file(self.ins.judge_no, self.ins)

    def delete_save_file(self, judge_no):
        file_name = "%s.pickle" % judge_no
        file_path = conf.JUDGING_FILE_DIR + "/" + file_name
        os.remove(file_path)

    def get_score(self, judge_no):
        file_name = "%s.pickle" % judge_no
        file_path = conf.JUDGING_FILE_DIR + "/" + file_name
        with open(file_path, "r") as f:
            self.ins = pickle.load(f)
        print self.ins.scores
        return self.ins.scores

    def get_judging(self):
        return self.ins

    def insert_score(self, judge_no, score):
        self.ins.append_score(score)
