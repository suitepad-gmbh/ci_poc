#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

import unittest


__all__ = ['TestAssertion']


class TestAssertion(unittest.TestCase):
    """
    Sample Assertion Tests
    """
    def test_0010_compare_strings(self):
        self.assertEquals('test', 'test')


def suite():
    "Test suite"
    test_suite = unittest.TestSuite()
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestAssertion)
    )
    return test_suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
