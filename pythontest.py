#!/usr/bin/python

import unittest
from python import returnThis

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testADS(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

class MoreTests(unittest.TestCase):

	def testMoreOne(self):
		self.failIf(IsOdd(2))

	def testMoreTwo(self):
		self.failUnless(IsOdd(1))

class PythonTests(unittest.TestCase):
	def testReturnValue(self):
		valueOfMethod = returnThis()
		self.failUnless(valueOfMethod == "ReturnString")

def main():
    unittest.main()

if __name__ == '__main__':
    main()