#!/usr/bin/python


from menu import Menu
import unittest


class doTests(unittest.TestCase):
    def test_menu_check_git_repos(self):
        Menu(user_input='1', test=True)
    def test_menu_check_for_uncommitted_repos(self):
        Menu(user_input='3', test=True)


if __name__ == '__main__':
    unittest.main()