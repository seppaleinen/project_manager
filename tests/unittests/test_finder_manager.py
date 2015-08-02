#!/usr/bin/python


import unittest, os
from python_dir.finder_manager import FinderManager
from python_dir.packagefile import get_workspace

workspace = os.getcwd()

class doTests(unittest.TestCase):
    def test_find_all_git_dirs(self):
        result = FinderManager().find_all_git_dirs(workspace)
        self.failUnless(result != None and result[0].endswith('.git'))

    def test_find_all_git_dirs_WORKSPACE(self):
        result = FinderManager().find_all_git_dirs(workspace)
        self.failIf(result == None)

if __name__ == '__main__':
    unittest.main()