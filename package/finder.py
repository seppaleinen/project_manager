#!/usr/bin/python

import os

def find_all_git_dirs(workspace):
    return [os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(workspace)
        for f in dirnames if f.endswith('.git')]