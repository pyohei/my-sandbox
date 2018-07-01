#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Score handler

Score operation handler"""


class Score(object):

    def __init__(self, kind):
        """ init about importer

        This module assume about import module.
        Argument of 'kind' indicates the way of judging.
        In __init__, dicide what module is need."""

        score_dir = kind
        score_module = kind.lower()

        """ Import only necessary module """
        import_module = "score.%s.%s" % (score_dir, score_module)
        from_list = ["Calculation, Registration"]
        self.main_module = __import__(import_module, fromlist=from_list)

    def calc(self, score):
        score_cls = self.main_module.Calculation(score)
        return score_cls.main()

    def register(self, score=1):
        score_reg = self.main_module.Registration(score)
        score_reg.main()

    def catch_total(self):
        return self.main_module.Overall()

if __name__ == "__main__":
    hand = Handler()
