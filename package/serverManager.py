#!/usr/bin/python


import subprocess


class ServerManager:
    def __init__(self, ps = "jboss"):
        self.ps = ps


    def check_jboss_status(self):
        ps = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE).communicate()[0]
        processes = ps.split("\n")
        for process in processes:
            if self.ps in process:
                return 'OK'