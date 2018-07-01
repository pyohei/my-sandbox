# -*- Coding: utf-8 -*-

import os
import re


def load_modules():
    dirs = os.listdir(os.path.abspath(os.path.dirname(__file__)))
    target_dirs = [d for d in dirs
                   if (re.match(r'.+py$', d) and d != '__init__.py')]
    return target_dirs
