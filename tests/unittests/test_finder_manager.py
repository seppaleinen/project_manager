#!/usr/bin/python


import unittest, os
from python_dir.finder_manager import find_all_git_dirs
from python_dir.packagefile import get_workspace


class doTests(unittest.TestCase):
    def test_find_all_git_dirs(self):
    	workspace = os.getcwd()
        result = find_all_git_dirs(workspace)
        self.failUnless(result != None and result[0].endswith('.git'))

    def test_find_all_git_dirs_WORKSPACE(self):
    	workspace = os.getcwd()
        result = find_all_git_dirs(workspace)
        self.failIf(result == None)

if __name__ == '__main__':
    unittest.main()