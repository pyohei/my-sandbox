#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Unit of OBO score

Haveing blow property
    - player_no
    - technicalmerit
    - presentation

"""

class ScoreBase(object):

    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx)

if __name__ == "__main__":
    s = ScoreBase()
    s.technicalmerit = 10
    s.presentation = 20
    print s.technicalmerit
    print s.presentation
