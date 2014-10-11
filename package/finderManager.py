#!/usr/bin/python

import os


def find_all_git_dirs(workspace):
    """
    find all git directories in workspace
    :param workspace:
    :return list:
    """
    return [os.path.join(dirpath, f)
            for dirpath, dirnames, files in os.walk(workspace)
            for f in dirnames if f.endswith('.git')]