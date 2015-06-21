# -*- coding: utf-8 -*-

"""

"""

import sys, os

def through_main_path():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    paths = dirpath.split("/")
    main_path = "/".join(paths[0:-1])
    sys.path.append(main_path)
through_main_path()

# CREATE bottle import setting
#CWD = os.getcwd()
#if not os.path.exists(CWD+"/wsgi/bottle/__init__.py"):
#    f = open(CWD+"/wsgi/bottle/__init__.py", "wb")
#    f.close()
#if not os.path.exists(CWD+"/wsgi/bottle/__init__.py"):
#    f = open(CWD+"/wsgi/bottle/__init__.py", "wb")
#    f.close()

#dirpath = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(dirpath)
#os.chdir(dirpath)
#os.chdir(os.path.dirname(__file__))

import bottle
import main

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
