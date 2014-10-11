#!/usr/bin/python

import unittest
from package.finder import *
from os.path import expanduser

class doTests(unittest.TestCase):
	def firstTest(self):
		find_all_git_dirs(expanduser("~"))

if __name__ == '__main__':
	unittest.main()