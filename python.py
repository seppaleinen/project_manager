#!/usr/bin/python

import sys, datetime

def iterateArray():
	mylist = []
	mylist.append("HEJ")
	mylist.append("HOJ")

	for a in mylist:
		print a

def readInput():
	x = raw_input("Enter digit ")
	if x is "1":
		print "if " + x
	else:
		print "else " + x

def takeArguments(arguments):
	for argument in arguments:
		print argument

def returnThis():
	a = "ReturnString"
	return a

def iterateBigArray():
	before = str(datetime.datetime.now())
	for a in range(0, 100000):
		x = a
	after = str(datetime.datetime.now())
	print "BEFORE: " + before
	print "AFTER: " + after

def main(args):
	print "BEGIN"

	readInput()

	iterateArray()

	takeArguments(args)

	value = returnValue()

	print "Value: " + value

	iterateBigArray()

	print "END"

if __name__ == "__main__":
   main(sys.argv[1:])