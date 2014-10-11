#!/usr/bin/python

import unittest
from package.packagefile import get_workspace
from os.path import expanduser


class doTests(unittest.TestCase):
    def test_get_workspace(self):
        workspace = get_workspace()
        home_dir = expanduser("~")
        self.failUnless(workspace != None)


if __name__ == '__main__':
    unittest.main()