"""Initialize testing."""

import os
import sys

try:
    if TESING_SETUP_LOADED:
        pass
except NameError:
    TESING_SETUP_LOADED = False


def init():
    if TESING_SETUP_LOADED:
        return
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    python_path = cur_dir.replace('test', 'src')
    sys.path.append(python_path)

init()
TESING_SETUP_LOADED = True
