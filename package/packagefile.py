#! /usr/bin/python

import os
import fnmatch

def returnWord():
	return "String"

def getWorkspace():
	workspace = os.environ['WORKSPACE']
	return workspace

def traverse():
    for cur, _dirs, files in os.walk("."):
        pref = ''
        head, tail = os.path.split(cur)
        while head:
            pref += '---'
            head, _tail = os.path.split(head)
        print(pref+tail)
        for f in files:
            print(pref+'---'+f)