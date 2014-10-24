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

    def test_compile_build_py(self):
        GIT_REPO=os.getcwd() + '/.git'
        pull_result='OK'
        compiler(GIT_REPO, pull_result)

    def test_compile_pom_xml(self):
        GIT_REPO=os.getcwd() + '/src/unittest/resources/pom/.git'
        pull_result='OK'
        compiler(GIT_REPO, pull_result)

    def test_compile_build_gradle(self):
        GIT_REPO=os.getcwd() + '/src/unittest/resources/gradle/.git'
        pull_result='OK'
        compiler(GIT_REPO, pull_result)

    def test_compile_setup_py(self):
        GIT_REPO=os.getcwd() + '/src/unittest/resources/setup/.git'
        pull_result='OK'
        compiler(GIT_REPO, pull_result)



if __name__ == '__main__':
    unittest.main()