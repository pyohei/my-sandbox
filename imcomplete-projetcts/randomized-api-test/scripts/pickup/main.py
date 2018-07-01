# -*- Coding: utf-8 -*-

""" Pick up api parameter(Test).

Pick up api parameter. But this module is test source.
"""

import os
import sys
python_path_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(python_path_dir.replace('/pickup', ''))

from creater import Creater
from parser import Parser
from reader import Reader
from retainer import Retainer


def main_test():
    reader = Reader()
    retainer = Retainer()
    params = reader.read()
    api_targets = []
    for name, param in params.items():
        parser = Parser(name, param)
        api_targets.append(parser)
    for target in api_targets:
        creater = Creater(target)
        api_parameters = creater.create()
        retainer.insert(target.name, api_parameters)
    retainer.close()

if __name__ == '__main__':
    main_test()
