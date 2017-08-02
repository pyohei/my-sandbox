# -*- Coding: utf-8 -*-

""" Parameter reader.

Read difined parameters.
"""


import importlib
import re
import parameters


class Reader(object):

    def __init__(self):
        pass

    def read(self):
        """Read parameter data."""
        modules = parameters.load_modules()
        if not modules:
            raise ValueError('No target parameters')
        return self.__load_params(modules)

    def __load_params(self, modules):
        params = {}
        for m in modules:
            param = {}
            exec_import = 'parameters.{0}'.format(
                m.replace('.py', ''))
            mod = importlib.import_module(exec_import)
            for i in mod.__dict__.items():
                if re.match(r'^__.+__$', i[0]):
                    continue
                param[i[0]] = i[1]
            params[m.replace('.py', '')] = param
        return params
