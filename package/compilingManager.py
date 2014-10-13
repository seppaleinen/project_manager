#!/usr/bin/python


import os
from os import listdir
from os.path import isfile, join


class CompilingManager():
    def __init__(self, dir_to_compile):
        self.dir_to_compile = dir_to_compile
        self.file_to_compile = self.__get_compiler_type()

    def __get_compiler_type(self):
        accepted_files = {'setup.py','pom.xml'}
        return [ f for f in listdir(self.dir_to_compile) if isfile(join(self.dir_to_compile,f)) and f in accepted_files ]