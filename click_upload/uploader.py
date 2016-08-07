#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Uploader file with one click

Need upload directory in argument.

"""

# import logging
import os
from explorer import Explorer
from connection import Connection
import uploader_conf


class Uploader:

    def __init__(self, base_dir=None):
        self.base_dir = base_dir
        self.base_dir = os.path.join(base_dir, uploader_conf.BASE_DIR)
        conn = Connection()
        self.connection = conn.get_connection()

    def upload(self):
        explorer = Explorer(self.base_dir)
        for filename in explorer.explore():
            self.__upload(filename)

    def __upload(self, filename):
        if self.__is_ignore(filename):
            return
        if self.__has_error(filename):
            if not uploader_conf.PART_UPLOAD:
                return
        r_path = self.__create_remote_path(filename)
        remote_path = os.path.join(
            uploader_conf.REMOTE_BASE, r_path[1:])
        self.connection.upload(filename, remote_path)

    def __init_log(self):
        pass

    def __is_ignore(self, filename):
        pass

    def __has_error(self, filename):
        pass

    def __create_remote_path(self, filename):
        return filename.replace(self.base_dir, "")

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option(
        "-d", "--dir", dest="base_dir",
        help="Indicate explore directory. If no, this treat './'",
        metavar="BASE_DIRECTORY")
    (option, args) = parser.parse_args()
    # This is for test.
    uploader = Uploader("")
    # uploader = Uploader(option["base_dir"])
    uploader.upload()
