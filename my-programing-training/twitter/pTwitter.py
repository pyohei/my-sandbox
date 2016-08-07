#!/usr/local/bin/python
#-*- coding: utf-8 -*-

"""
This module is twiiter handler.
We can utillze under function.

-submit
 can submit "str", "int" "list".
 If possible, not post long sentence and many list.
 Upper kind may happen error.
 I don't check about this error.

"""

import tweepy

class PTwitter(object):

    # setting account information
    def __init__(self, account):
        self.consumer_key = account["consumer_key"]
        self.consumer_secret = account["consumer_secret"]
        self.access_key = account["access_key"]
        self.access_secret = account["access_secret"]
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(auth_handler=auth)

    # submit tweet
    def submit(self, murmur):
        if isinstance(murmur, int):
            murmur = [str(murmur)]
        if not isinstance(murmur, list):
            raise
        contents = self.__process(murmur)
        for content in contents:
            self.api.update_status(content)

    # process tweet contents
    def __process(self, murmur):
        talks = []
        for talk in murmur:
            talk = str(talk).decode("utf-8")
            if len(talk) <= 140:
                talks.append(talk)
                continue
            # long coment has possibility occuring error!
            # and in this souce need to check!
            say = ""
            for s in talk:
                say += s
                if len(say) > 135:
                    talks.append(say)
                    say = ""
            talks.append(talk)
        return talks


