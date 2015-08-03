#!/usr/bin/python


import unittest, os, sys
from python_dir.menu import Menu
from StringIO import StringIO

workspace = os.getcwd() + '/.git'

class doIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        self.out = StringIO()
        sys.stdout = self.out

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_menu_check_git_repos(self):
        os.environ["WORKSPACE"] = workspace
        Menu(user_input='1', test=True)
        output = self.out.getvalue().strip()

    def test_menu_update_git_repos(self):
        os.environ["WORKSPACE"] = workspace
        Menu(user_input='2', test=True)
        output = self.out.getvalue().strip()

    def test_menu_check_for_uncommitted_repos(self):
        os.environ["WORKSPACE"] = workspace
        Menu(user_input='3', test=True)
        output = self.out.getvalue().strip()

