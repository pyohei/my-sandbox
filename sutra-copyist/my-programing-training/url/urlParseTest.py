#!/usr/local/bin/python
#-*- coding: utf-8 -*-

# Created: 2014/2/26
import urllib
import urllib2
import cookielib

def get_page(url):
    urlInfo = urllib.urlencode({})
    # print urlInfo
    request = urllib2.Request(url, urlInfo, {})
    # print request
    response = urllib2.urlopen(request)
    # print response
    return response.read()

import re

def searchKafunInfo(page):
    RE_TABLE = re.compile('<TABLE.*?>(.*?)</TABLE>',re.DOTALL) # .を改行にもマッチさせる
    RE_MAINTABLE = re.compile('HTTP')
    for m in re.finditer(RE_TABLE,page):
        table_text = m.group(1)
        if RE_MAINTABLE.search(table_text):
            return table_text
    return None


# page = get_page("").decode("euc-jp")
page = get_page("")
print page

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
      HTMLParser.__init__(self)
      self.links = {}
      self.linkurl = ''

    # aタグのみ処理を行い、href属性の内容をlinkurlに格納
    def handle_starttag(self, tag, attrs):
      if tag == 'img':
        attrs = dict(attrs)
        if 'src' in attrs:
          self.linkurl = attrs['src']

    # これは書かなくてもよい
    def handle_endtag(self, tag):
      pass

    # linkurlに値が入っている場合のみ、（つまりAタグの場合）
    # urlをキー：アンカーテキストをバリューとしてディクショナリに追加
    def handle_data(self, data):
      if self.linkurl:
        self.links[self.linkurl] = data
        self.linkurl = ''

parser = MyHTMLParser()
# parser.feed(page)
tag = "img"
attrs = [("src", "")]

parser = MyHTMLParser()
parser.feed(page.decode("utf-8"))
parser.close()

cnt = 0
pollen_forecast = {}
for k, v in parser.links.items():

    if cnt > 1:
        break

    k_str = k.encode('utf-8')
    v_str = re.sub('^[ \n\r\t]+|[ \n\r\t]+$', '', v).encode('utf_8')

    if "" in k_str:
        if cnt == 0:
            pollen_forecast["tomorrow"] = v_str
            cnt += 1
        if cnt == 1:
            pollen_forecast["today"] = v_str
            cnt += 1

def parse_pollen():
    return pollen_forecast
