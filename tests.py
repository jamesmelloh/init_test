#tests.py

import sys
import os
try:
    print('JENKINS_WORKSPACE' + os.environ.get('JENKINS_HOME'))
except KeyError:
    print('KeyError')

import pytest
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_pass(self):
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        self.assertEqual(11, 7 + 3)# tests.py

suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
unittest.TextTestRunner(verbosity=2).run(suite)
