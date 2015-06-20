#!/usr/local/bin/python
# -*- coding: utf-8 -*-


from wsgi.bottle import bottle_connector as base
from wsgi.bottle.bottle import bottle

bottle.run(host='localhost', port=8080, debug=True)
