#!/usr/bin/python


import os


class FinderManager(object):
    def find_all_git_dirs(self, workspace):
        """
        find all git directories in workspace
        :param workspace:
        :return list:
        """
        return [os.path.join(dirpath, f)
                for dirpath, dirnames, files in os.walk(workspace)
                for f in dirnames if f.endswith('.git') and files is not None]