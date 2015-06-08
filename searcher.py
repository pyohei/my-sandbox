# -*- coding: utf-8 -*-

from __future__ import absolute_import
#from handler import Handler

class Searcher(object):

    def __init__(self, handler="cloudsearch"):
        """
        Initialize search setting

        :param handler: search way ["cloudsearch"]
        :type handler: string
        """
        self.handler = Hander(handler)

    def handle(self, domain=None):
        self.handler.domain = domain

    def get(self, request):
        result = self.handler.get(request)
        return result

    def post(self, reqest):
        result = self.handler.post(request)

if __name__ == "__main__":
    pass
