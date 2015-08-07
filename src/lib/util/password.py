#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Password operator.

This module give the function about password.
  generator -- generate password
"""

import hashlib
import random


WORDS = ("abcdefghijkmnopqrstuvwxyz"
         "ABCDEFGHIJKLMNPQRSTUVWXYZ123456789"
         "_$@#!%^*&:?;=_")


def generator(num=8):
    if num < 4:
        raise ValueError("There are vulnerability in your argument.")
    passwd = ""
    for n in range(num):
        pass_num = random.randint(0, int(len(WORDS)) - 1)
        passwd += WORDS[pass_num]
    return passwd


def encrypt(passwd, encry_type="sha224"):
    _encrypt = eval("hashlib.%s()" % encry_type)
    try:
        encry = _encrypt
    except:
        encry = hashlib.sha224()
    encry.update(passwd)
    return encry.hexdigest()

if __name__ == '__main__':
    pass
