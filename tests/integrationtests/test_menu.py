#!/usr/bin/python

import unittest, os
from python_dir.menu import Menu

workspace = os.getcwd() + '/.git'

class doIntegrationTest(unittest.TestCase):
    def test_menu_check_git_repos(self):
        os.environ["WORKSPACE"] = workspace
        Menu(user_input='1', test=True)

    def test_menu_update_git_repos(self):
        os.environ["WORKSPACE"] = workspace
        Menu(user_input='2', test=True)

    def test_menu_check_for_uncommitted_repos(self):
        os.environ["WORKSPACE"] = workspace
        Menu(user_input='3', test=True)
