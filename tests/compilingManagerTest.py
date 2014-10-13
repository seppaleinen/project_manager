#!/usr/bin/python


import unittest
import os
from package.compilingManager import CompilingManager


class doTests(unittest.TestCase):
    def test_find_all_git_dirs(self):
        compilingManager = CompilingManager(os.getcwd())
        dir_to_compile = compilingManager.dir_to_compile
        file_to_compile = compilingManager.file_to_compile
        self.failUnless(dir_to_compile == os.getcwd())
        self.failUnless(file_to_compile[0] == 'setup.py')


if __name__ == '__main__':
    unittest.main()