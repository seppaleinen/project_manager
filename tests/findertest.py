#!/usr/bin/python

import unittest
from package.finder import *
from package.packagefile import get_workspace


class doTests(unittest.TestCase):
    def test_find_all_git_dirs(self):
        result = find_all_git_dirs(os.getcwd())
        self.failUnless(result != None and result[0].endswith('.git'))

    def test_find_all_git_dirs_WORKSPACE(self):
        workspace = get_workspace()
        result = find_all_git_dirs(workspace)
        self.failIf(result == None)

if __name__ == '__main__':
    unittest.main()