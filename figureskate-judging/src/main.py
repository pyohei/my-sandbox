#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Figureskate-judging-system main.

Figureskate-judging main script.
HTTP requests thorough this module to parse url and execute modules.

URL Lists:
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
import sys
import os
"""
def init():
    CWD = os.getcwd()
    print CWD
    sys.path.append(CWD)
    if os.path.exists(CWD+"/bottle/__init__.py"):
        return
    f = open(CWD+"/bottle/__init__.py", "wb")
    #if os.path.exists(CWD+"/wsgi/bottle/bottle/__init__.py"):
    #    return
    #f = open(CWD+"/wsgi/bottle/bottle/__init__.py", "wb")
    f.close()
init()
"""


def init():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    print dirpath
    os.chdir(dirpath)
init()

try:
    from bottle import route
except:
    sys.path.append(
        os.path.join(os.path.dirname(__file__), 'framework/bottle/'))
    from bottle import route

from datetime import datetime
from datetime import timedelta

from bottle import run
from bottle import template
# from bottle import get
# from bottle import post
from bottle import request
from bottle import response
from bottle import static_file
from api.score.score import Score
from api.contest.entry import Entry as cEnt
from api.contest import handler as cHandler
from api.contest.judging import Judging
from api.contest.select.selector import Selector as cSelector
from api.contest.register.register import Register as cRegister
# from api.contest.result.handler import Handler as r_handler
from api.player.entry import Entry as pEnt
from api.judge.entry import Entry as jEnt
from api.judge.editing.editing import Editing as j_Editing
from api.judge.editing.update import Update as j_Update
from lib.util import session
from config import config as conf

# Import script file


@route("/js/<filepath:path>")
def import_javascript(filepath):
    return static_file(filepath, root="./public/js")


@route("/css/<filepath:path>")
def import_css(filepath):
    return static_file(filepath, root="./public/css")


# Interpretation URL
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
    selector = cSelector()
    contests = selector.select()
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/contest/select.tpl",
        main_contents={"contests": contests},
        css_files=["/css/contest/selector.css"])


@route("/judge/judging")
@route("/judge/judging", method="post")
@route("/judge/result", method="post")
def judge_test():
    """ Juging method.

    Between judging start and end, through this module.

    Managemento of judgement depends on pickle file
    named judge_no('judge_no'.pickle)
    """
    score = ""
    # contest_no = 0
    if not has_valid_cookie:
        return __return_login_form()
    s = session.init()
    cookie = get_cookie()
    judge_no = s.select_judge_no(cookie[0][1])
    if not judge_no:
        raise ValueError("Not register user!! Call manager.")
    requests = parse_request(request.forms)
    print "request:", requests
    print "judge no:", judge_no
    c_handler = cHandler.init()
    # Display more than second
    if requests and "contest_no" not in requests:
        score = format_score(judge_no, requests)
        c_handler.load(judge_no)
        c_handler.insert_score(judge_no, score)
        judging = c_handler.get_judging()
        print "is_end", judging.is_end()
        if judging.is_end():
            c_handler.delete_save_file(judge_no)
            __input_score(judging)
            return template(
                "views/root/base",
                tpl_func_file="views/root/judge/result",
                main_contents=None,
                css_files=["/css/judge/judge.css"])
        judging.next()
        c_handler.save()
    # First Display
    if "contest_no" in requests:
        judging = Judging(judge_no, int(requests["contest_no"]))
        c_handler.create_judging_file(judge_no, judging)
    # player_no = judging.player_no
    game = {"url": judging.movie_url,
            "is_end": judging.is_end()}
    return template(
        "views/root/base",
        tpl_func_file="views/root/judge/judge",
        main_contents=game,
        css_files=["/css/judge/judge.css"])


@route("/contest/register")
@route("/contest/register", method="post")
def contest_register():
    requests = parse_request(request.forms)
    if not requests:
        return template(
            "views/root/base",
            tpl_func_file="views/root/contest/register",
            main_contents=None,
            css_files=[])
    r = cRegister(requests)
    r.register()
    return template(
        "views/root/base",
        tpl_func_file="views/root/contest/register",
        main_contents=None,
        css_files=[])


@route("/judge/editing")
def edit_judge():
    """ Editing judge profile"""
    if not has_valid_cookie:
        return __return_login_form()
    s = session.init()
    cookie = get_cookie()
    judge_no = s.select_judge_no(cookie[0][1])
    editing = j_Editing(judge_no)
    profiles = editing.load_profile()
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/judge/editing.tpl",
        main_contents={"profiles": profiles},
        css_files=["/css/contest/selector.css"])


@route("/judge/update", method="post")
def update_judge():
    """ Update judge profile"""
    if not has_valid_cookie:
        return __return_login_form()
    s = session.init()
    cookie = get_cookie()
    judge_no = s.select_judge_no(cookie[0][1])
    requests = parse_request(request.forms)
    j_update = j_Update(judge_no)
    j_update.update(requests)
    return __return_main()


@route("/contest/result", method="get")
@route("/contest/result", method="post")
def show_contest_result():
    if not has_valid_cookie:
        return __return_login_form()
    # s = session.init()
    # cookie = get_cookie()
    # judge_no = s.select_judge_no(cookie[0][1])
    """
    requests = parse_request(request.forms)
    handler = r_handler(judge_no)
    result = handler.arrange(requests)
    """
    result = {
        "contest_name": "テスト大会",
        "rank": [
            {'judge_num': 14,
             'player_no': 1L,
             'presentation': 1.5,
             'technical_merit': 1.4,
             'total': 1.4,
             'player_name': 'ぴよぴよ'
             },
            {'judge_num': 13,
             'player_no': 2L,
             'presentation': 1.3,
             'technical_merit': 1.2,
             'total': 1.3,
             'player_name': 'ほげほげ'
             }
        ]
    }
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/contest/result.tpl",
        main_contents=result,
        css_files=["/css/conteset/result.css"])


@route("/logout")
def logout():
    del_cookie()
    return __return_login_form()

# ------- Manager screen ------- #


@route("/management/main")
def management_main():
    # if not has_valid_cookie():
    #     return login_menue()
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/management/main.tpl",
        main_contents=None,
        css_files=[])


@route("/management/entry/<func>")
def test2(func):
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/management/%s_register/register.tpl" % (
            func),
        main_contents=None,
        css_files=[])


@route("/management/result", method="post")
def result():
    # my_requests = parse_request(request.forms)
    # func = my_requests["func"]
    # if func == "judge":
    #     entry_judge(my_requests)
    # if func == "contest":
    #     entry_contest(my_requests)
    # if func == "player":
    #     entry_player(my_requests)
    tpl_func_file = "response_ok"
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/management/player_register/%s.tpl" % (
            tpl_func_file),
        main_contents=None,
        css_files=[])


# Functions
def __input_score(judging):
    """ input score into database """
    judge_type = conf.JUDGING_TYPE[judging.judge_type]
    sc = Score(judge_type)
    # result = sc.calc(judging.scores)
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
    response.set_cookie(
        "session_id",
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
    # import os
    # print os.getcwd()
    # os.chdir("../")
    # print os.getcwd()
    # os.chdir("../")
    # print os.getcwd()
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/login.tpl",
        main_contents=None,
        css_files=[])


def __return_main():
    return template(
        "views/root/base.tpl",
        tpl_func_file="views/root/menue.tpl",
        main_contents=None,
        css_files=[])

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
