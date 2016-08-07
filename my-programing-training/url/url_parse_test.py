#!/usr/local/bin/python
#-*- coding: utf-8 -*-

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

print get_page("")
