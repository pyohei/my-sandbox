#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""""
This is HTML Parser wrapper.
html.py is abstract module, and reaarange according to purpose.

Next step, I want to make useful definision used this.

reference URL is
http://docs.python.jp/2/library/htmlparser.html?
highlight=htmlparser#HTMLParser
"""

from HTMLParser import HTMLParser

class Parser(HTMLParser):

    # init. This makes HTMLParser instance.
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = ""
        self.num = 0

    # reset instance
    def reset(self):
        HTMLParser.reset(self)

    # called by empty-element-tag like <a .... />
    def handle_startendtag(self, tagname, attribute):
        print "6666", tagname
        print "7777", attribute

    # called by tag, get tag name and tag attribute
    # first argument is tag name, second is attributes
    #   ex) [('id', 'python'), ('name', 'java')]
    def handle_starttag(self, tagname, attribute):
        print "0000",tagname
        print "1111",self.get_starttag_text()
        print "2222",attribute
        print self.num
        self.num += 1
        if self.num == 100:
            print "yes"

    # called by end tag
    def handle_endtag(self, endtag):
        print "3333",endtag

    # called by other text
    def handle_data(self, data):
        print "4444",data
        print "5555",self.get_starttag_text()

    # called by character reference
    def handle_charref(self, refname):
        print "9999",refname

    # called by [&gt;(>) or &lt;(<)]
    def handle_entityref(self, refname):
        print "aaaa",refname

    # called by comment(<!--text-->...->text)
    def handle_comment(self, commentvalue):
        print "bbbb",commentvalue

    # called by SGML decaration (<!...>)
    def handle_decl(self, declname):
        print "cccc",declname

    # called by unknown SGML decaration (<!...>)
    def unknown_decl(self, declname):
        print "dddd",declname

    # called by Processing Instruction (<?xml vvarsion=1.0...>)
    def handle_pi(self, piname):
        print "eeee",piname

# console execute
if __name__ == '__main__':
    c = """
    <?xml version='1.0' encodint='utf-8'>
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
    <head>
    <title>HTMLParser test</title>
    </head>
    <body>
    <p>これはテストです</p>
    <ul>
      <li>りんご</li>
      <li>ゴリラ</li>
    </ul>
    <br><br>
    <table id='test' name='TEST'>
      <tr>
        <th>ヘッダー</th>
        <th>header</th>
      </tr>
      <tr>
        <td>内容</td>
        <td>contents</td>
      </tr>
    </table>
    </body>
    </html>
    """
    h = Parser()
    # -- to get (line_num, offset_num) --
    # print h.getpos()
    # -- feed send singnal to parse HTML --
    h.feed(c)
    # -- after parsing, need closing --
    h.close()
