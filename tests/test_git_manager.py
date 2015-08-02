#!/usr/bin/python


from python_dir.git_manager import *
import os
import unittest
import mock


project_dir = os.getcwd()


class doTests(unittest.TestCase):
    def test_git_pull(self):
        result = git_pull(project_dir)
        self.failUnless(result == 'OK')
    def test_git_checkout(self):
        branch = "master"
        result = git_checkout(project_dir, branch)
        self.failUnless(result == 'OK')
    def test_git_check_for_updates(self):
        result = git_check_for_updates(project_dir)
        #self.failUnless(result is None)
    def test_git_check_for_uncommitted_changes(self):
        git_check_for_uncommitted_changes(project_dir)
    @mock.patch('python_dir.git_manager.Repo')
    def test_git_pull_pass_error(self, mocked):
        mocked.return_value = mocked
        mocked.git._call_process.side_effect = GitCommandError('Error', 'Error')
        self.assertRaises(GitCommandError, git_pull(project_dir))
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with("pull")


if __name__ == '__main__':
    unittest.main()