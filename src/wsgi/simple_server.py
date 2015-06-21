# -*- coding: utf-8 -*-

import os
import sys
try:
    import bottle
except:
    print "This Server don't install bottle.py..."
    # If you don't have bottle.py, import from local.
    def through_bottle_path():
        dirpath = os.path.dirname(os.path.abspath(__file__))
        paths = dirpath.split("/")
        bottle_paths = paths[0:-1] + ["framework", "bottle"]
        bottle_path = "/".join(bottle_paths)
        sys.path.append(bottle_path)
    through_bottle_path()
    import bottle
# base.py is wsgi connector. This system's radical source.
import base
bottle.run(host='localhost', port=8080, debug=True)
