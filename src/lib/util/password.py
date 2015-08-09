#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Password operator.

This module give the function about password.

Attributes:
    generator (int): Generate password.

    encrypt (str): Encrypt string. You can use to encrypt password.
        If you use `generator()`, you should this module'
"""

import hashlib
import random

WORDS = ("abcdefghijkmnopqrstuvwxyz"
         "ABCDEFGHIJKLMNPQRSTUVWXYZ123456789"
         "_$@#!%^*&:?;=_")


def generator(num=8):
    """Generate password.

    >>> generator(8) == generator(8)
    False
    """
    if num < 4:
        raise ValueError("There are vulnerability in your argument.")
    passwd = ""
    for n in range(num):
        pass_num = random.randint(0, int(len(WORDS)) - 1)
        passwd += WORDS[pass_num]
    return passwd


def encrypt(passwd, encry_type="sha224"):
    """Encrypt password.

    >>> encrypt('hogehoge') == encrypt('hogehoge')
    True
    """
    _encrypt = eval("hashlib.%s()" % encry_type)
    try:
        encry = _encrypt
    except ImportError:
        encry = hashlib.sha224()
    encry.update(passwd)
    return encry.hexdigest()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
