#!/usr/bin/python


import unittest, os, sys, mock
from python_dir.menu import Menu, compiler
from StringIO import StringIO

resources_dir = os.getcwd() + '/tests/resources'

class doCompilerTests(unittest.TestCase):
    def test_compile_pom_xml(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            GIT_REPO=resources_dir + '/pom/.git'
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
            GIT_REPO=resources_dir + '/gradle/.git'
            pull_result='OK'
            compiler(GIT_REPO, pull_result)

            output = out.getvalue().strip()
            expected_output = 'Compile ' + resources_dir + '/gradle/build.gradle'
            assert output == expected_output
        finally:
            sys.stdout = saved_stdout

    def test_compile_setup_py(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            GIT_REPO=resources_dir + '/setup/.git'
            pull_result='OK'
            compiler(GIT_REPO, pull_result)

            output = out.getvalue().strip()
            expected_output = 'Compile ' + resources_dir + '/setup/setup.py'
            assert output == expected_output
        finally:
            sys.stdout = saved_stdout

    def test_compile_build_py(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            GIT_REPO=resources_dir + '/pybuild/.git'
            pull_result='OK'
            compiler(GIT_REPO, pull_result)

            output = out.getvalue().strip()
            expected_output = 'Compile ' + resources_dir + '/pybuild/build.py'
            assert output == expected_output
        finally:
            sys.stdout = saved_stdout


class doMenuTests(unittest.TestCase):
    def test_menu_unknown_command(self):
        Menu(user_input='4', test=True)

    @mock.patch('__builtin__.raw_input')
    def test_menu_no_input(self, mocked):
        Menu(test=True)
        mocked.assert_called_with('')

    @mock.patch('python_dir.menu.get_workspace')
    @mock.patch('python_dir.menu.git_check_for_updates')
    @mock.patch('python_dir.menu.FinderManager')
    def test_check_git_repos(self, find_mock, check_updates_mock, workspace_mock):
        workspace_mock.return_value = "workspace"
        find_mock.return_value = find_mock
        find_mock.find_all_git_dirs.return_value = [ 'git_repo' ]
        check_updates_mock.return_value = [ 'master' ]

        menu = Menu(user_input='1', test=True)

        workspace_mock.assert_called_with()
        find_mock.find_all_git_dirs.assert_called_with(mock.ANY)
        check_updates_mock.assert_called_with('git_repo')

    @mock.patch('python_dir.menu.compiler')
    @mock.patch('python_dir.menu.git_pull')
    @mock.patch('python_dir.menu.git_checkout')
    @mock.patch('python_dir.menu.get_workspace')
    @mock.patch('python_dir.menu.git_check_for_updates')
    @mock.patch('python_dir.menu.FinderManager')
    def test_update_git_repos(
        self, 
        find_mock, 
        git_check_mock, 
        workspace_mock, 
        checkout_mock, 
        pull_mock, 
        compiler_mock
        ):
        workspace_mock.return_value = 'workspace'
        find_mock.return_value = find_mock
        find_mock.find_all_git_dirs.return_value = [ 'git_repo' ]
        git_check_mock.return_value = [ 'branch' ]

        Menu(user_input='2', test=True)

        workspace_mock.assert_called_with()
        find_mock.find_all_git_dirs.assert_called_with('workspace')
        git_check_mock.assert_called_with('git_repo')
        checkout_mock.assert_called_with('git_repo', 'branch')
        pull_mock('git_repo')
        compiler_mock('git_repo', mock.ANY)

    @mock.patch('python_dir.menu.get_workspace')
    @mock.patch('python_dir.menu.git_check_for_updates')
    @mock.patch('python_dir.menu.FinderManager')
    def test_update_git_repos_no_updates(
        self,
        find_mock,
        git_check_mock,
        workspace_mock
        ):
        workspace_mock.return_value = 'workspace'
        find_mock.return_value = find_mock
        find_mock.find_all_git_dirs.return_value = [ 'git_repo' ]
        git_check_mock.return_value = []

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            Menu(user_input='2', test=True)
            output = out.getvalue().strip()
            self.assertTrue('All Branches in git_repo is updated' in output)
        finally:
            sys.stdout = saved_stdout

        workspace_mock.assert_called_with()
        find_mock.find_all_git_dirs.assert_called_with('workspace')
        git_check_mock.assert_called_with('git_repo')

    @mock.patch('python_dir.menu.get_workspace')
    @mock.patch('python_dir.menu.git_check_for_uncommitted_changes')
    @mock.patch('python_dir.menu.FinderManager')
    def test_check_for_uncommitted_changes(
        self,
        find_mock,
        git_changes_mock,
        workspace_mock
        ):
        workspace_mock.return_value = 'workspace'
        find_mock.return_value = find_mock
        find_mock.find_all_git_dirs.return_value = [ 'git_repo' ]

        Menu(user_input='3', test=True)

        workspace_mock.assert_called_with()
        find_mock.find_all_git_dirs.assert_called_with('workspace')
        git_changes_mock.assert_called_with('git_repo')


if __name__ == '__main__':
    unittest.main()