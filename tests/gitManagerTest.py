#!/usr/bin/python

from package.gitManager import *

import unittest

class doTests(unittest.TestCase):
	def test_git_pull(self):
		git_repo = "/Users/shaman_king_2000/IdeaProjects/python"
		result = git_pull(git_repo)
		self.failUnless(result != None)
	def test_git_checkout(self):
		git_repo = "/Users/shaman_king_2000/IdeaProjects/python"
		branch = "master"
		result = git_checkout(git_repo, branch)
		self.failUnless(result != None)
	def test_git_check_for_updates(self):
		git_repo = "/Users/shaman_king_2000/IdeaProjects/python"
		result = git_check_for_updates(git_repo)
		#self.failUnless(result != None)

if __name__ == '__main__':
    unittest.main()