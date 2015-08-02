#!/usr/bin/python


from python_dir.git_manager import *
import os
import unittest
import mock


project_dir = os.getcwd()


class doTests(unittest.TestCase):
    @mock.patch('python_dir.git_manager.Repo')
    def test_git_pull(self, mocked):
        mocked.return_value = mocked
        result = git_pull(project_dir)
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with('pull')
        self.failUnless(result == 'OK')

    @mock.patch('python_dir.git_manager.Repo')
    def test_git_pull_pass_error(self, mocked):
        mocked.return_value = mocked
        mocked.git._call_process.side_effect = GitCommandError('Error', 'Message')
        self.assertRaises(GitCommandError, git_pull(project_dir))
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with("pull")

    @mock.patch('python_dir.git_manager.Repo')
    def test_git_checkout(self, mocked):
        mocked.return_value = mocked
        branch = "master"
        result = git_checkout(project_dir, branch)
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with('checkout', branch)
        self.failUnless(result == 'OK')

    @mock.patch('python_dir.git_manager.Repo')
    def test_git_checkout_pass_error(self, mocked):
        mocked.return_value = mocked
        mocked.git._call_process.side_effect = GitCommandError('Error', 'Message')
        branch = "master"
        self.assertRaises(GitCommandError, git_checkout(project_dir, branch))
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with('checkout', branch)

    @mock.patch('python_dir.git_manager.Repo')
    def test_git_check_for_updates(self, mocked):
        mocked.return_value = mocked
        mocked.git._call_process.return_value = "git result \n master pushes to master (local out of date)"
        result = git_check_for_updates(project_dir)
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with('remote', 'show', 'origin')
        self.failIf(result is [])
        self.failUnless('master' in result)

    @mock.patch('python_dir.git_manager.Repo')
    def test_git_check_for_updates_no_result(self, mocked):
        mocked.return_value = mocked
        result = git_check_for_updates(project_dir)
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with('remote', 'show', 'origin')
        self.assertEqual(result, [])

    @mock.patch('python_dir.git_manager.Repo')
    def test_git_check_for_uncommitted_changes(self, mocked):
        mocked.return_value = mocked
        mocked.git._call_process.return_value = "Changes not staged for commit"
        result = git_check_for_uncommitted_changes(project_dir)
        mocked.assert_called_with(project_dir)
        mocked.git._call_process.assert_called_with('status')    


if __name__ == '__main__':
    unittest.main()