#!/usr/bin/python

from git import *


def git_pull(git_repo):
    """
	git pull git_repo
	"""
    repo = Repo(git_repo)
    origin = repo.remotes.origin
    return origin.pull()


def git_checkout(git_repo, branch):
    """
	git checkout git_repo branch
	"""
    repo = Repo(git_repo)
    git = repo.git
    return git.checkout(branch)


def git_check_for_updates(git_repo):
    """
	Check for updates on remote
	Does git remote show origin,
	then if there are out of dates
	parse the branch-name from row and return
	"""
    repo = Repo(git_repo)
    result = repo.git._call_process("remote", "show", "origin")
    gitResultRows = result.split("\n")
    for row in gitResultRows:
        if "(local out of date)" in row:
            return row.split("pushes to ")[1].split(" (local out of date")[0]