"""Test of envloader"""

import unittest

import test_initialize
import envloader


class TestEnvloader(unittest.TestCase):

    def setUp(self):
        test_initialize.init()

    def test_load(self):
        env = envloader.load(PREFIX='HOME')
        self.assertIsNotNone(env.HOME)

if __name__ == '__main__':
    unittest.main()
