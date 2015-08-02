#!/usr/bin/python

import unittest
from python_dir.packagefile import get_workspace, input_from_user
from os.path import expanduser
import mock


class doTests(unittest.TestCase):
    def test_get_workspace(self):
        workspace = get_workspace()
        home_dir = expanduser("~")
        self.failIf(workspace is None)

    @mock.patch('__builtin__.input')
    def test_get_input(self, mocked):
    	mocked.return_value = 'Return'
    	result = input_from_user()
    	self.assertEqual('Return', result)


if __name__ == '__main__':
    unittest.main()