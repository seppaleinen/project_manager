#!/usr/bin/python


import unittest
from python_dir.server_manager import ServerManager


class doTests(unittest.TestCase):
    def test_check_ps_for_python(self):
        result = ServerManager(ps='python').check_jboss_status()
        self.failIf(result is None)
    def test_get_jboss_base_dir(self):
        result = ServerManager(ps='python').get_jboss_dir(split_delimiter='python ')
        self.failIf(result is None)


if __name__ == '__main__':
    unittest.main()