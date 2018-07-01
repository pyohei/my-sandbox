# -*- coding: utf-8 -*-

import sys
import os

try:
    from setuptools import setup
except:
    from distutiles.core import setup

if sys.version_info < (2,7):
    raise NotImplemented("Your Python version is not treated. Reccomend 2.7")

def set_bottle_path():
    path = os.path.dirname(__file__)
    bottle_path = os.path.join(path, "src/framework/bottle")
    sys.path.append(bottle_path)

try:
    import bottle
except ImportError:
    print "your pc don't bottle"
    set_bottle_path()
    import bottle

def set_base_path():
    path = os.path.dirname(__file__)
    main_path = os.path.join(path, "src")
    sys.path.append(main_path)

set_base_path()
import main
