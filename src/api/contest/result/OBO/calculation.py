#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Calculation OBO score

This module calculate obo score and rank.
Return score ranking as below.

"""


class Calculation(object):

    def __init__(self, contest_no):
        self.contest_no = contest_no

    def calculate(self, scores):
        s = {}
        tec = {}
        pre = {}
        for score in scores:
            player = score["player_no"]
            user = score["judge_user"]
            _tec = score["technical_merit"]
            _pre = score["presentation"]
            if player not in tec:
                tec[player] = {user: _tec}
                pre[player] = {user: _pre}
            else:
                tec[player][user] = _tec
                pre[player][user] = _pre
        s["technical_merit"] = tec
        s["presentation"] = pre
        scores = []
        for n in s["technical_merit"].keys():
            result = {}
            judge_num = len(s["technical_merit"][n].keys())
            tec_sum = sum(s["technical_merit"][n].values())
            pre_sum = sum(s["presentation"][n].values())
            result["player_no"] = n
            result["technical_merit"] = round(
                tec_sum / judge_num * 0.1, 1)
            result["presentation"] = round(
                pre_sum / judge_num*0.1, 1)
            result["total"] = round((result["technical_merit"] +
                                     result["presentation"]) / 2.0, 1)
            result["judge_num"] = judge_num
            scores.append(result)
        import pprint
        pp = pprint.PrettyPrinter(indent=2)
        ranks = sorted(scores, key=lambda x: x["total"], reverse=True)
        pp.pprint(ranks)
        return s

if __name__ == "__main__":
    from loader import Loader
    l = Loader(1)
    r = l.load()
    c = Calculation(1)
    s = c.calculate(r)
