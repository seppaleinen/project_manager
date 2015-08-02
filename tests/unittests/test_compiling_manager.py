#!/usr/bin/python

import sys, os, unittest
from python_dir.compiling_manager import CompilingManager


class TestCase(unittest.TestCase):
    def test_compiling_manager_init(self):
        compilingManager = CompilingManager(os.getcwd())
        dir_to_compile = compilingManager.dir_to_compile
        file_to_compile = compilingManager.file_to_compile
        self.failUnless(dir_to_compile == os.getcwd())
        self.failUnless(file_to_compile == dir_to_compile + '/' + 'setup.py')

    def test_compiling_manager_no_result(self):
        cwd = os.getcwd() + '/scripts'
        compilingManager = CompilingManager(cwd)
        self.assertEqual(compilingManager.file_to_compile, compilingManager.dir_to_compile + '/')


if __name__ == '__main__':
    unittest.main()