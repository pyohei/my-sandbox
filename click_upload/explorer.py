#!/usr/local/bin/python
# -*- coding: utf-8 -*-


"""

"""

import os
import uploader_conf

class Explorer(object):

    def __init__(self, base_dir):
        self.base_dir = base_dir

    def explore(self):
        for dir_path, dirs, filenames in os.walk(self.base_dir):
            for filename in filenames:
                yield os.path.join(dir_path, filename)

if __name__ == "__main__":
    path = "/Users/mukaishohei/Programing/dev/www/figurejudge"
    ex = Explorer(path)
    for f in ex.explore():
        print f
