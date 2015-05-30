#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Register of contest.

Register contest detail.

"""

from header.register import Register as hRegister
from detail.register import Register as dRegister

CONTEST_HEADER = [
    "contest_name",
    "contest_date",
    "contest_type",
    "judge_type",
    "contest_image"
    ]

CONTEST_DETAIL = [
    "movie_link",
    "start_time",
    "end_time",
    "player"
    ]
CONTEST_DETAIL_OPTION = [
    "start_time",
    "end_time"
    ]

MAX_PLAYER = 20
LIMIT_PLAYER = 3

class Register(object):

    def __init__(self, form):
        self.form = form
        self.header = {}
        self.details = []

    def register(self):
        self.__parse()
        h_register = hRegister()
        d_register = dRegister()
        h_register.register(self.header)
        contest_no = h_register.get_contest_no()
        d_register.register(self.details, contest_no)

    def __parse(self):
        self.__distribute_header()
        self.__distribute_ditail()

    def __distribute_header(self):
        for header in CONTEST_HEADER:
            self.header[header] = self.form[header]

    def __distribute_ditail(self):
        for n in range(1, MAX_PLAYER):
            is_option = 0
            container = {}
            for detail in CONTEST_DETAIL:
                if detail in CONTEST_DETAIL_OPTION:
                    is_option = 1
                detail += str(n)
                if detail not in self.form:
                    break
                container[detail] = self.form[detail]
                if is_option and not container[detail]:
                    container[detail] = 0
            if not container:
                break
            self.details.append(container)
        if n < LIMIT_PLAYER:
            raise ValueError(
                "Need movie more than 4! ")

if __name__ == "__main__":
    form = {
        'movie_link3': 'http://youyou.xxxyyy',
        'contest_name': 'test',
        'contest_date': '2014/11/11',
        'contest_type': '3',
        'judge_type': '2',
        'contest_image': 'test.jpg',
        'end_time4': '2',
        'end_time5': '1000',
        'end_time2': '40',
        'end_time3': '20',
        'start_time4': '1',
        'end_time1': '20',
        'player2': '5',
        'player3': '3',
        'player1': '1',
        'player4': '4',
        'player5': '2',
        'start_time3': '3',
        'start_time2': '2',
        'movie_link4': 'http://iiii.ooo.ww',
        'movie_link5': 'http://iuou.dijfdi.dd',
        'movie_link2': 'http://youtube.com/di?dddd=kii://',
        'start_time1': '1',
        'start_time5': '90',
        'movie_link1': 'http://xxxx.yyy'}
    r = Register(form)
    r.register()
