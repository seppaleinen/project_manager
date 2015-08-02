#!/usr/bin/python


import unittest, os, mock
from python_dir.packagefile import get_workspace, input_from_user


class doTests(unittest.TestCase):
    def test_get_workspace(self):
        os.environ["WORKSPACE"] = os.getcwd()
        workspace = get_workspace()
        self.failIf(workspace is None)
        self.assertEqual(os.getcwd(), workspace)

    @mock.patch('__builtin__.input')
    def test_get_input(self, mocked):
    	mocked.return_value = 'Return'
    	result = input_from_user()
    	self.assertEqual('Return', result)


if __name__ == '__main__':
    unittest.main()