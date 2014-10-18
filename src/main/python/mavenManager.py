#!/usr/bin/python


import subprocess


class MavenManager():
    def mavify_pom_file(self, path_to_pom):
        maven_result = subprocess.Popen(['mvn', 'clean', 'install', '-f', path_to_pom],
                                        stdout=subprocess.PIPE).communicate()[0]
        if 'BUILD SUCCESS' in maven_result:
            return 'OK'