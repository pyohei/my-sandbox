#!/usr/local/bin/python
# -*- coding: utf-8 -*-


""" Handle score.

Decide judge_type, create instance, and set scores.

"""

JUDGE_DEF = {
    1: "obo",
    2: "cop"}


def init():
    global __handler_instance
    if __handler_instance:
        return __handler_instance
    __handler_instance = Movie()
    return __handler_instance


class Handler(object):

    def __init__(self):
        self._clear()

    def _clear(self):
        self.cls = None

    def insert_score(self, player_no, judge_type, scores):
        self._clear()
        judge_name = JUDGE_DEF[judge_type]
        upper_judege_name = judge_name.capitalize()
        cls_name = "from contest.score.%s import %s as Cls" % (
            judge_name,
            upper_judege_name)
        exec(cls_name)
        self.cls = Cls(player_no, scores)

    def get_instance(self):
        return self.cls.get_instance()

if __name__ == "__main__":
    scores = {
        "technical_merit_first": 1,
        "technical_merit_second": 3,
        "presentation_first": 4,
        "presentation_second": 7
        }
    handle = Handler()
    handle.insert_score(1, scores)
    ins = handle.get_instance()
    print ins.technicalmerit
    print ins.presentation
