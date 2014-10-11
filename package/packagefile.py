#!/usr/bin/python

import os

def get_workspace():
    """
    Tries to get WORKSPACE env variable
    default is home directory
    :return workspace:
    """
    return os.getenv('WORKSPACE', "~/")


def input_from_user():
    """
    Asks for input from user
    :return input:
    """
    return input('What directory?: ')