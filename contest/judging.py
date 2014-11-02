#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Contest selector

Select contest for judge.

*old type*
In first, I'm thinkng throuw the argment with dict, like blow.
contents = {
    "contest_no": 1,
    "skating_order": [2, 1],
    "judging_type": 1,
    "entry_time": datetime.now(),
    "score": []
    }

*new style*
Next, I adapt instance.

"""

from datetime import datetime
from random import shuffle
from contest.detail.movie import Movie
from contest.detail.detail import Detail
from contest.score.handler import Handler as ScoreHandler

class Judging(object):

    def __init__(self, judge_no, contest_no):
        self.pop = 0
        self._contest_no = contest_no
        self._judge_no = judge_no
        self._players = []
        self._urls = []
        self._entry_time = None
        self._scores = []
        self._judge_type = 0
        self.__load(self._contest_no)

    def next(self):
        self.pop += 1

    def is_end(self):
        return len(self._players) == self.pop + 1

    def append_score(self, score):
        # 'ScoreHandler' equal with 'contest.score.handler.Handler'
        handler = ScoreHandler()
        handler.insert_score(
            self.player_no,
            self._judge_type,
            score)
        self._scores.append(handler.get_instance())
        print "a"
        print self._scores

    def __load(self, contest_no):
        detail = Detail()
        recs = detail.load(contest_no)
        self.__set_detail(recs)

    def __set_detail(self, recs):
        for rec in recs:
            self._players.append(rec["player_no"])
        self._judge_type = rec["judge_type"]
        self._entry_time = rec["contest_date"]
        shuffle(self._players)

    # ---- property list -----
    @property
    def contest_no(self):
        return self._contest_no

    @property
    def judge_no(self):
        return self._judge_no

    @property
    def player_no(self):
        return self._players[self.pop]

    @property
    def movie_url(self):
        player_no = self._players[self.pop]
        movie = Movie()
        return movie.get_url(player_no)

    @property
    def entry_time(self):
        return self._entry_time

    @property
    def judge_type(self):
        return self._judge_type

    @property
    def scores(self):
        return self._scores

if __name__ == "__main__":
    j = Judging(1, 1)
    print j.contest_no
    print j.judge_no
    print j.player_no
    print j.movie_url
    print j.entry_time
    print j.isEnd()
    j.next()
    print j.player_no
    print j.movie_url
    print j.isEnd()
