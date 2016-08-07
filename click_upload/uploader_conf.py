#!/usr/local/bin/python
# -*- coding: utf-8 -*-


""" Upload File Configuration

Configuration.

Created: 2014-11-30
"""
# PART_UPLOAD decide wheather upload or not.
# If `True`, upload files except error file.
# And `False`, not upload if having error file.
PART_UPLOAD = False

# Wheather making directory if not.
MAKE_DIR = False

# Wheather making directory if not.
MAKE_FILE = False

# Connection type
#   1 ... SCP
#   2 ... FTP
CONNECTION_TYPE = 1

# Ignore File type (not implemented)
IGNORE_FILE_TYPE = [r"*.pyc"]

# Log directory
LOG_DIR = ""

# Look Directory
#   This tool search files below the `BASE_DIR`.
#   If not, check directory from argument directory.
BASE_DIR = "scr"

# Remote value
REMOTE_BASE = "/home/user"

# SCP Connection Setting
SCP_HOST = ""
SCP_PORT = 22
SCP_USERNAME = ""
SCP_PASSWORD = ""

# FTP Connection Setting
FTP_HOST = ""
FTP_USER = ""
FTP_PASS = ""
