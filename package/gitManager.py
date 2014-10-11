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
	"""
	repo = Repo(git_repo)
	git = repo.git
	result = git