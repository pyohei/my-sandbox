#!/usr/local/bin/python
#-*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString

domTest = parse("./test.xml")

print domTest
