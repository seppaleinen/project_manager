#! /usr/bin/python

import os
import fnmatch

def returnWord():
	return "String"

def getWorkspace():
	workspace = os.environ['WORKSPACE']
	return workspace

def traverse(directory):
    for cur, _dirs, files in os.walk(directory):
        pref = ''
        head, tail = os.path.split(cur)
        while head:
            pref += '---'
            head, _tail = os.path.split(head)
        print(pref+tail)
        for f in files:
            print(pref+'---'+f)