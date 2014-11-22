#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Figure skating judging main

Figure skating judging main system.
All programu pass this module.

*CONSTITUSION OF URL*
    /login ... Display login screen.
               Doing login though not having session, always use this
               screen.

    /menu .... Menue. Many function control in this screen.

    /judge/<judge type>/select
               Select contest to judge.
               The screen is different with judge type.

    /judge/judging/contestX
               Judging screen.
               'X' indicates contest number.

    /judge/result/contestX
               Judging result of contest 'X'.

    /logout .. Logout.

    /management/main
               Manager screen. Having blow function.
                 - entry judge
                 - entry player
                 - entry contest

"""

from bottle import route
from bottle import run
from bottle import template
#from bottle import get
#from bottle import post
from bottle import request
from bottle import response
from bottle import static_file
from datetime import datetime
from datetime import timedelta

import config as conf
from score.score import Score
from contest.entry import Entry as cEnt
from contest import handler as cHandler
from contest.judging import Judging
from contest.register.register import Register as cRegister
from player.entry import Entry as pEnt
from judge.entry import Entry as jEnt
from lib.util import session


###                                                             ###
### Root functions -------------------------------------------- ###
###                                                             ###

@route("/js/<filepath:path>")
def import_javascript(filepath):
    print filepath
    print "aaa"*10
    return static_file(filepath, root="./cms/js")

@route("/css/<filepath:path>")
def import_css(filepath):
    print filepath
    print "aaa"*10
    return static_file(filepath, root="./cms/css")

@route("/login")
def login():
    """ Display login form"""
    if has_valid_cookie():
        return management_main()
    return __return_login_form()

@route("/menu")
@route("/menu", method="post")
def menu():
    """ Menue screen management

    - Having valid cookie
        Go menue
    - Having invalid (or not having) cookie and valid login data
        Go menue
    - Having invalid (or not having) invalid cookie and valid login data
        Go login form
    """
    if has_valid_cookie():
        return __return_main()
    login_user = parse_request(request.forms)
    if not login_user:
        return __return_login_form()
    s = session.init()
    isOk = s.can_login(
        login_user["user_id"], login_user["password"])
    if isOk:
        register_cookie = s.publish(login_user)
        set_cookie(register_cookie)
        return __return_main()
    return __return_login_form()

@route("/judge/select")
def select_contest():
    return template("./cms/tpl/base.tpl",
        tpl_func_file="./cms/tpl/contest/select.tpl",
        main_contents=None)

@route("/judge/test")
@route("/judge/test", method="post")
@route("/judge/result", method="post")
def judge_test():
    """ Juging method.

    Between judging start and end, through this module.

    Managemento of judgement depends on pickle file
    named judge_no('judge_no'.pickle)
    """
    score = ""
    contest_no = 0
    if not has_valid_cookie:
        return __return_login_form()
    s = session.init()
    cookie = get_cookie()
    judge_no = s.select_judge_no(cookie[0][1])
    if not judge_no:
        raise ValueError, "Not register user!! Call manager."
    requests = parse_request(request.forms)
    c_handler = cHandler.init()
    if requests and "contest_no" not in requests:
        score = format_score(judge_no, requests)
        c_handler.load(judge_no)
        c_handler.insert_score(judge_no, score)
        judging = c_handler.get_judging()
        if judging.is_end():
            c_handler.delete_save_file(judge_no)
            __input_score(judging)
            return template("./cms/tpl/base",
                tpl_func_file="./cms/tpl/judge/result",
                main_contents=None)
        judging.next()
        c_handler.save()
    if "contest_no" in requests:
        judging= Judging(judge_no, int(requests["contest_no"]))
        c_handler.create_judging_file(judge_no, judging)
    player_no = judging.player_no
    game = {"url": judging.movie_url,
            "is_end": judging.is_end()}
    return template("./cms/tpl/base",
        tpl_func_file="./cms/tpl/judge/judge",
        main_contents=game)

@route("/contest/register")
@route("/contest/register", method="post")
def contest_register():
    requests = parse_request(request.forms)
    print requests
    if not requests:
        return template("./cms/tpl/base",
            tpl_func_file="./cms/tpl/contest/register",
            main_contents=None)
    r = cRegister(requests)
    r.register()
    return template("./cms/tpl/base",
        tpl_func_file="./cms/tpl/contest/register",
        main_contents=None)


@route("/logout")
def logout():
    del_cookie()
    return __return_login_form()

# ------- Manager screen ------- #

@route("/management/main")
def management_main():
    if not has_valid_cookie():
        return login_menue()
    return template("./cms/tpl/base.tpl",
        tpl_func_file="./cms/tpl/management/main.tpl",
        main_contents=None)

@route("/management/entry/<func>")
def test2(func):
    return template("./cms/tpl/base.tpl",
        tpl_func_file="./cms/tpl/management/%s_register/register.tpl" % (
            func),
        main_contents=None)

@route("/management/result", method="post")
def result():
    my_requests = parse_request(request.forms)
    func = my_requests["func"]
    if func == "judge":
        entry_judge(my_requests)
    if func == "contest":
        entry_contest(my_requests)
    if func == "player":
        entry_player(my_requests)
    tpl_func_file = "response_ok"
    return template("./cms/tpl/base.tpl",
        tpl_func_file="./cms/tpl/management/player_register/%s.tpl" % (
            tpl_func_file),
        main_contents=None)

# ----------- FUNCTION ------------ #

def __input_score(judging):
    """ input score into database """
    judge_type = conf.JUDGING_TYPE[judging.judge_type]
    sc = Score(judge_type)
    result = sc.calc(judging.scores)
    # in OBO way, calcultation don't use.
    # but other way, I am not thingking of it
    sc.register(judging)

def __entry_contest(contest):
    entry = cEnt(contest)
    entry.register()

def __entry_player(player):
    entry = pEnt(player)
    entry.register()
    return True

def __entry_judge(judge):
    entry = jEnt(judge)
    entry.register()

def set_cookie(cookie):
    now = datetime.now()
    expires_datetime = now + timedelta(days=conf.COOKIE_EXPIRES_DAYS)
    response.set_cookie("session_id",
        cookie["session_id"],
        expires=expires_datetime
        )

def get_cookie():
    return request.cookies.items()

def del_cookie():
    response.delete_cookie("session_id")

def parse_request(requests):
    req = {}
    for k, v in requests.items():
        req[k] = v
    return req

def format_score(judge_no, request):
    """ need to improve in this module """
    score = {}
    tec_first = int(request["technical_merit_first"])
    tec_second = int(request["technical_merit_second"])
    pre_first = int(request["presentation_first"])
    pre_second = int(request["presentation_second"])
    score["score"] = {}
    score["score"]["technicalmerit"] = tec_first * 10 + tec_second
    score["score"]["presentation"] = pre_first * 10 + pre_second
    # Undecidion how to read below data.
    score["contest_no"] = 1
    score["player_no"] = 2
    score["skating_no"] = 2
    score["judge_user"] = judge_no
    return score["score"]

def has_valid_cookie():
    cookie = get_cookie()
    if not cookie:
        return False
    s = session.init()
    return s.has(cookie[0][1])

def __return_login_form():
    return template("./cms/tpl/base",
        tpl_func_file="./cms/tpl/login",
        main_contents=None)

def __return_main():
    return template("./cms/tpl/base",
        tpl_func_file="./cms/tpl/menue",
        main_contents=None)

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
