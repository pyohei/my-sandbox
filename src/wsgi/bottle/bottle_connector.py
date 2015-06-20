# Change working directory so relative paths (and template lookup) work again
import sys, os

# CREATE bottle import setting
CWD = os.getcwd()
if not os.path.exists(CWD+"/wsgi/bottle/__init__.py"):
    f = open(CWD+"/wsgi/bottle/__init__.py", "wb")
    f.close()
#if not os.path.exists(CWD+"/wsgi/bottle/__init__.py"):
#    f = open(CWD+"/wsgi/bottle/__init__.py", "wb")
#    f.close()

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)
#os.chdir(os.path.dirname(__file__))

from bottle import bottle
#import figureskate_main
import main
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
