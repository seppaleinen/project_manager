#!/usr/bin/python


import unittest
from package.serverManager import ServerManager


class doTests(unittest.TestCase):
    def test(self):
        result = ServerManager(ps="python").check_jboss_status()
        self.failIf(result is None)


if __name__ == '__main__':
    unittest.main()