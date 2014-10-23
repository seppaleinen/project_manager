#!/usr/bin/python


from menu import Menu, compiler
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

    def test_compile(self):
        GIT_REPO=os.getcwd() + '/.git'
        pull_result='OK'
        compiler(GIT_REPO, pull_result)


if __name__ == '__main__':
    unittest.main()