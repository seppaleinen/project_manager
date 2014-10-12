#!/usr/bin/python

from package.packagefile import get_workspace
from package.finderManager import find_all_git_dirs
from package.gitManager import git_checkout
from package.gitManager import git_check_for_updates
from package.gitManager import git_pull


class Menu():
    def __init__(self):
        loop = True
        while loop:
            print('-----------------------------------------')
            print('What would you like to do?: enter empty to exit')
            print('1: Check which gitrepos needs updating')
            print('2: Update, build and deploy all outdated gitrepos')
            user_input = raw_input('')
            if user_input == '1':
                self.check_git_repos()
            elif user_input == '2':
                self.update_git_repos()
            else:
                loop = False

    def check_git_repos(self):
        for GIT_REPO in find_all_git_dirs(get_workspace()):
            branch = git_check_for_updates(GIT_REPO)
            if branch is not None:
                print "Branch %s in %s is outdated" % (branch, GIT_REPO)

    def update_git_repos(self):
        for GIT_REPO in find_all_git_dirs(get_workspace()):
            branch = git_check_for_updates(GIT_REPO)
            if branch is not None:
                print "Branch %s in %s is outdated" % (branch, GIT_REPO)
                checkout_result = git_checkout(GIT_REPO, branch)
                pull_result = git_pull(GIT_REPO)
            else:
                print "All Branches in %s is updated" % (GIT_REPO)