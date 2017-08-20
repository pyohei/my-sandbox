#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
.. Created: 2014-04-17
"""

# Adapter, one of the design pattern

class Adapter:
    def __init__(self,word):
        self.word = word

    def title(self):
        if "title" in self.word:
            return word["title"]
        return "not difined"

    def contents(self):
        if "contents" in self.word:
            return word["contents"]
        return "not difined"

    def sender(self):
        if "from" in self.word:
            return word["from"]
        return "not difined"

class Letter:
    def recv(self, letterPack):
        print "From:%s" % letterPack.sender()
        print "Title: %s " % letterPack.title()
        print "%s" % letterPack.contents()

if __name__ == "__main__":
    word = {
        "title":"Hello",
        "from":"stranger",
        "contents":"Hi! Are you doing?"}
    l = Letter()
    l.recv(Adapter(word))
