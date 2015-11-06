#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read(["./conf.ini"])
print config.get("Section", "long")
print config.get("Section", "foodir")
print config.defaults()
print config.sections()
print config.options("Section")

it = config.items("Judging Type")
print dict(it)


