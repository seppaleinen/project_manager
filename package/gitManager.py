#!/usr/bin/python

from git import *


def git_pull(git_repo):
    """
    git pull git_repo
    :param git_repo:
    :return result:
    """
    repo = Repo(git_repo)
    try:
        repo.git._call_process("pull")
    except GitCommandError:
        pass
    else:
        return 'OK'


def git_checkout(git_repo, branch):
    """
    git checkout git_repo branch
    :param git_repo:
    :param branch:
    :return result:
    """
    repo = Repo(git_repo)
    try:
        repo.git._call_process("checkout", branch)
    except GitCommandError:
        pass
    else:
        return 'OK'
#    git = repo.git
#    return git.checkout(branch)


def git_check_for_updates(git_repo):
    """
  	Check for updates on remote
	Does git remote show origin,
	then if there are out of dates
	parse the branch-name from row and return

    :param git_repo:
    :return result:
    """
    repo = Repo(git_repo)
    result = repo.git._call_process("remote", "show", "origin")
    git_result_rows = result.split("\n")
    for row in git_result_rows:
        if "(local out of date)" in row:
            return row.split("pushes to ")[1].split(" (local out of date")[0].strip()