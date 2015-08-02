#!/usr/bin/python


import unittest, os, sys
from python_dir.compiling_manager import CompilingManager

project_dir = os.getcwd()

class TestCase(unittest.TestCase):
    def test_compiling_manager_init(self):
        compilingManager = CompilingManager(project_dir)
        dir_to_compile = compilingManager.dir_to_compile
        file_to_compile = compilingManager.file_to_compile
        self.failUnless(dir_to_compile == project_dir)
        self.failUnless(file_to_compile == dir_to_compile + '/' + 'setup.py')

    def test_compiling_manager_no_result(self):
        scripts_dir = project_dir + '/scripts'
        compilingManager = CompilingManager(scripts_dir)
        self.assertEqual(compilingManager.file_to_compile, compilingManager.dir_to_compile + '/')


if __name__ == '__main__':
    unittest.main()