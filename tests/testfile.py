#!/usr/bin/python

import unittest
from package.packagefile import return_word
from package.packagefile import get_workspace
from os.path import expanduser


class doTests(unittest.TestCase):
    def testFirst(self):
        self.failUnless(return_word() == "String")
    def test_get_workspace(self):
    	workspace = get_workspace()
    	home_dir = expanduser("~")
        self.failUnless(workspace != None)

def main():
    unittest.main()


if __name__ == '__main__':
    main()