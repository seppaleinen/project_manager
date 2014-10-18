#!/usr/bin/python


import unittest
from serverManager import ServerManager


class doTests(unittest.TestCase):
    def test_check_ps_for_python(self):
        result = ServerManager(ps='pyb').check_jboss_status()
        self.failIf(result is None)
        self.failUnless('pyb' in result)
    def test_get_jboss_base_dir(self):
        result = ServerManager(ps='pyb').get_jboss_dir(split_delimiter='python ')
        print('result=%s' % (result,))
        self.failIf(result is None)
        self.failIf('pyb' not in result)


if __name__ == '__main__':
    unittest.main()