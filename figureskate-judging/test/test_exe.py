# -*- coding: utf-8 -*-

import sys, os

dirpath = os.path.dirname(os.path.abspath(__file__))
paths = dirpath.split("/")
main_path = "/".join(paths[0:-1])
project_path = main_path + "/src"
sys.path.append(project_path)

import unittest
from lib.util import password

class PasswordTest(unittest.TestCase):

    def setUp(self):
        print "set up"

    def test_generator(self):
        self.assertTrue(password.generator(10))

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(PasswordTest))
    return suite

if __name__ == "__main__":
    unittest.main()
