#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Handler of result view

"""

from lib.record import recordFactory

IMP_MOD = "from %s.%s import %s"

class Handler(object):

    def __init__(self, judge_no):
        self.judge_no = judge_no
        self.conn = recordFactory.init().get_connection()

    def arrange(self, result):
        result = {}
        contest_no = result["contest_no"]
        cls_name = self.__extract_contest_cls(contest_no)
        mods = self.__make_imp_string(cls_name)
        for mod in mods:
            exec(mod)
        loader = Loader(contest_no)
        targets = loader.load()
        calc = Calculation(contest_no)
        rank = calc.calculate(targets)
        result["rank"] = rank
        viewer = Viewer(contest_no)
        result["template"] = viewer.template
        return result

    def __extract_contest_cls(contest_no):
        """ must fix to load from database """
        conn = self.conn
        return "OBO"

    def __make_imp_string(cls_name):
        mods = []
        cls_list = ["Calculation", "Loader", "Viewer"]
        for cls in cls_list:
            cls = IMP_MOD % (cls_name.upper(), cls.lower(), cls)
            mods.append(cls)
        return mods
