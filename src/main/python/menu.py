#!/usr/bin/python


from packagefile import get_workspace
from finder_manager import find_all_git_dirs
from git_manager import git_checkout
from git_manager import git_check_for_updates
from git_manager import git_pull
from git_manager import git_check_for_uncommitted_changes
from compiling_manager import CompilingManager
from maven_manager import MavenManager


def compiler(GIT_REPO, pull_result):
    if pull_result == 'OK':
        dir_to_compile = GIT_REPO.replace('/.git', '')
        build_file = CompilingManager(dir_to_compile).file_to_compile
        if 'pom.xml' in build_file:
            compile_result = MavenManager().mavify_pom_file(build_file)
            print('Compileresult: %s' % (compile_result,))
        if 'setup.py' in build_file:
            print('Compile %s' % (build_file))
        if 'build.gradle' in build_file:
            print('Compile %s' % (build_file))
        if 'build.py' in build_file:
            print('Compile %s' % (build_file))


class Menu():
    def __init__(self, user_input=None, test=False):
        loop = True
        while loop:
            print('-----------------------------------------')
            print('What would you like to do?: enter empty to exit')
            print('1: Check which gitrepos needs updating')
            print('2: Update, build and deploy all outdated gitrepos')
            print('3: Check for uncommitted changes')
            if user_input is None:
                user_input = raw_input('')
            if user_input == '1':
                self.check_git_repos()
            elif user_input == '2':
                self.update_git_repos()
            elif user_input == '3':
                self.check_for_uncommitted_changes()
            else:
                loop = False
            if test:
                loop = False

    def check_git_repos(self):
        """
        Iterate through all gitrepositories
        run git remote show origin | grep local out of date
        and print results
        :return None:
        """
        for GIT_REPO in find_all_git_dirs(get_workspace()):
            branch_list = git_check_for_updates(GIT_REPO)
            if branch_list:
                for branch in branch_list:
                    print "Branch %s in %s is outdated" % (branch, GIT_REPO)

    def update_git_repos(self):
        """
        Iterate through all gitrepositories
        run git remote show origin | grep 'local out of date'
        checkout all outdated repositories and pull
        then check if pom.xml, setup.py, or build.gradle exists
        and compile.
        :return None:
        """
        for GIT_REPO in find_all_git_dirs(get_workspace()):
            branch_list = git_check_for_updates(GIT_REPO)
            if branch_list:
                for branch in branch_list:
                    print "Branch %s in %s is outdated" % (branch, GIT_REPO)
                    checkout_result = git_checkout(GIT_REPO, branch)
                    pull_result = git_pull(GIT_REPO)
                    compiler(GIT_REPO, pull_result)
            else:
                print "All Branches in %s is updated" % (GIT_REPO)

    def check_for_uncommitted_changes(self):
        """
        Iterate through all gitrepositories
        run git status | grep Changes not staged for commit
        and print result
        :return:
        """
        for GIT_REPO in find_all_git_dirs(get_workspace()):
            result = git_check_for_uncommitted_changes(GIT_REPO)
            if result is not None:
                print(result)