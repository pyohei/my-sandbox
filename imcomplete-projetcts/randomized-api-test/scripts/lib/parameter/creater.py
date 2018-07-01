# -*- Coding: utf-8 -*-

""" Parameter creater.

"""

import os
from lib.random import 

PROJECT_ROOT = '/Users/mukaishohei/Programing/dev/tool/randomized-aptest/scripts/project'


class Creater(object):

    def __init__(self, api_num=None, api_type='json', project_name=None)
        self.api_num = api_num
        self.api_type = api_type
        self.project_name = project_name
        self.__load()


    def __load(self):
        project_dir = os.path.join(PROJECT_ROOT, self.project_name)
        for root, dirs, files in os.walk(project_dir):





