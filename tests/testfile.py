#!/usr/bin/python

import unittest
from package.packagefile import returnWord

class doTests(unittest.TestCase):
	def testFirst(self):
		self.failUnless(returnWord() == "String")

def main():
    unittest.main()

if __name__ == '__main__':
    main()