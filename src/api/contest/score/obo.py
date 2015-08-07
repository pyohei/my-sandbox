#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Unit of OBO score

Haveing blow property
    - player_no
    - technicalmerit
    - presentation

"""

from datetime import datetime
from contest.score.base import ScoreBase


class Obo(object):

    def __init__(self, player_no, scores):
        self.instance = ScoreBase()
        self.scores = scores
        self.player_no = player_no
        self.__set()

    def get_instance(self):
        return self.instance

    def __set(self):
        # self.__process()
        self.now = datetime.now()
        self.instance.player_no = self.player_no
        self.instance.technicalmerit = self.scores["technicalmerit"]
        self.instance.presentation = self.scores["presentation"]

    def __process(self):
        print self.scores
        self.scores["technicalmerit"] = (
            self.scores["technical_merit_first"] * 10 +
            self.scores["technical_merit_second"])
        self.scores["presentation"] = (
            self.scores["presentation_first"] * 10 +
            self.scores["presentation_second"])

if __name__ == "__main__":
    scores = {
        "technical_merit_first": 1,
        "technical_merit_second": 3,
        "presentation_first": 4,
        "presentation_second": 7
        }
    obo = Obo(scores)
    ins = obo.get_instance()
    print ins
    print ins.technicalmerit
    print ins.presentation
