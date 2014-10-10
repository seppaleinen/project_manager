#!/usr/bin/python

import os
from subprocess import call


def return_word():
    return "String"


def get_workspace():
    return os.environ['WORKSPACE']


def traverse(directory):
    for cur, files in os.walk(directory):
        pref = ''
        head, tail = os.path.split(cur)
        while head:
            pref += '---'
            head, _tail = os.path.split(head)
        print(pref + tail)
        for f in files:
            print(pref + '---' + f)


def input_from_user():
    return input('What directory?: ')


def execute_command(command):
    call([command])