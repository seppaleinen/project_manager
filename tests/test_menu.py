#!/usr/bin/python


from python_dir.menu import Menu, compiler
import os
import unittest
import sys
from StringIO import StringIO


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
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            GIT_REPO=os.getcwd() + '/tests/resources/pom/.git'
            pull_result='OK'
            compiler(GIT_REPO, pull_result)

            output = out.getvalue().strip()
            assert output == 'Compileresult: OK'
        finally:
            sys.stdout = saved_stdout

    def test_compile_build_gradle(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            GIT_REPO=os.getcwd() + '/tests/resources/gradle/.git'
            pull_result='OK'
            compiler(GIT_REPO, pull_result)

            output = out.getvalue().strip()
            expected_output = 'Compile ' + os.getcwd() + '/tests/resources/gradle/build.gradle'
            assert output == expected_output
        finally:
            sys.stdout = saved_stdout

    def test_compile_setup_py(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            GIT_REPO=os.getcwd() + '/tests/resources/setup/.git'
            pull_result='OK'
            compiler(GIT_REPO, pull_result)

            output = out.getvalue().strip()
            expected_output = 'Compile ' + os.getcwd() + '/tests/resources/setup/setup.py'
            assert output == expected_output
        finally:
            sys.stdout = saved_stdout



if __name__ == '__main__':
    unittest.main()