#!/usr/bin/python


import unittest
import os
from python_dir.maven_manager import MavenManager


project_dir = os.getcwd()


class doTests(unittest.TestCase):
    def test_mavify_pom_file(self):
        result = MavenManager().mavify_pom_file('%s/tests/resources/pom/pom.xml' % (project_dir,))
        self.failIf(result is None)
        self.failUnless(result == 'OK')


if __name__ == '__main__':
    unittest.main()
