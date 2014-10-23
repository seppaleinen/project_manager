#!/usr/bin/python


from menu import Menu
import os
import unittest


class doTests(unittest.TestCase):
    def test_menu_check_git_repos(self):
        os.environ["WORKSPACE"] = os.getcwd() + "/.git"
        Menu(user_input='1', test=True)

    def test_menu_update_git_repos(self):
        os.environ["WORKSPACE"] = os.getcwd() + "/.git"
        Menu(user_input='2', test=True)

    def test_menu_check_for_uncommitted_repos(self):
        os.environ["WORKSPACE"] = os.getcwd() + "/.git"
        Menu(user_input='3', test=True)


if __name__ == '__main__':
    unittest.main()