#!/usr/bin/python

import os
import subprocess

def return_word():
    return "String"


def get_workspace():
    """
    Tries to get WORKSPACE env variable
    default is home directory
    """
    return os.getenv('WORKSPACE', "~/")


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
    """
    Asks for input from user
    """
    return input('What directory?: ')


def execute_command(command):
    """
    Execute external command
    returns result of command or None if error
    """
    try:
        return subprocess.check_output(["cd", "/opt"])
    except OSError:
        return None
