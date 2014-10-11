#!/usr/bin/python


import unittest


class doTests(unittest.TestCase):
	def firstTest(self):
		self.failIf(self is None)


if __name__ == '__main__':
	unittest.main()