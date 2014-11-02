#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Judgeing test

You should play the test with this module.
If appending new way, you should make new class.
In testing, change console execute code into what you use
system.

-- protocol --
class TestXxxx
    def __init__(self):
        # This module insert score
        # ex) self.score = {"xxx": 4, "yyyy":5}
        ***MUST CONTENT***
          contest_no ... game name
          plya_no ... the number of play order

    def excecute(self):
        # This module execute main module.
        # Execute "main()" module in "judge.py"
        # (Argument must be judge type(Folder name).
        # ex) judge.main("XXX")
"""

import figureskate_main as judge

class TEST_SCORE_OBO(object):

    def __init__(self):
        self.score = {
                "score": {"technical_merit": 5.5,
                          "presentation": 2.8
                          },
                "contest_no": 1,
                "player_no": 1,
                "skating_no": 1,
                "judge_user": 1
                }


    def execute(self):
        judge.main("OBO", self.score)

class TEST_INPUT_CONTEST(object):

    def __init__(self):
        self.contest = {
                "contest_name": "フリー大会",
                "contest_type": 1,
                "judge_type": 1,
                "contest_date": "2014-02-01",
                }

    def execute(self):
        judge.entry_contest(self.contest)


class TEST_INPUT_PLAYER(object):

    def __init__(self):
        self.player = {
                "player_name": "ぴよぴよ",
                "player_nickname": "ぴよ",
                "degree": 2,
                "country": 2
                }

    def execute(self):
        judge.entry_player(self.player)

class TEST_INPUT_JUDGE(object):

    def __init__(self):
        self.judge = {
                "judge_first_name":"ぴよぴよ",
                "judge_last_name":"テスト",
                "judge_nickname": "piyo",
                "judge_capacity": 1,
                "email": "piyopiyo@test.com",
                "register_time": "2014-08-25"
                }

    def execute(self):
        judge.entry_judge(self.judge)
        #judge.entry_judge(self.judge)

if __name__ == "__main__":
    ts = TEST_SCORE_OBO()
    ts.execute()
    tc = TEST_INPUT_CONTEST()
    tc.execute()
    tp = TEST_INPUT_PLAYER()
    tp.execute()
    tj = TEST_INPUT_JUDGE()
    tj.execute()
