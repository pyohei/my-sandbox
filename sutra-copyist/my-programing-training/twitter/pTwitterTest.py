#!/usr/local/bin/python
#-*- coding: utf-8 -*-

# Created: 2014-03-02


consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

from twitter.pTwitter import PTwitter

account = {"consumer_key": "",
    "consumer_secret": "",
    "access_key": "",
    "access_secret": ""}

t = PTwitter(account)

texts = ["あ","い", "u", "e", "o", "b" "t"]

t.submit(["ろ"])
