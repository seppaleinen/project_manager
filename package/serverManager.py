#!/usr/bin/python


import subprocess


class ServerManager:
    def __init__(self, ps="jboss"):
        self.ps = ps

    def check_jboss_status(self):
        """
        Check ps -ef for jboss
        return result
        :return String:
        """
        processes = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE).communicate()[0].split("\n")
        for process in processes:
            if self.ps in process:
                return process

    def get_jboss_dir(self, split_delimiter='jboss.server.base.dir='):
        """
        Check ps -ef for split_delimiter, default jboss.server.base.dir=
        split result to path
        :param split_delimiter:
        :return String:
        """
        process = self.check_jboss_status()
        if process is not None:
            return process.split(split_delimiter)[1].split(' ')[0]