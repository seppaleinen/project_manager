#!/usr/bin/python

import os
from subprocess import call

def returnWord():
	return "String"

def getWorkspace():
	workspace = os.environ['WORKSPACE']
	return workspace

def traverse(directory):
    for cur, files in os.walk(directory):
        pref = ''
        head, tail = os.path.split(cur)
        while head:
            pref += '---'
            head, _tail = os.path.split(head)
        print(pref+tail)
        for f in files:
            print(pref+'---'+f)

def inputFromUser():
	return input('What directory?: ')

def executeCommand(command):
	call([command])