#! /usr/bin/env python3

import unittest
from continuous_mutation.python_filter.pyfilter import Filter

pyfilter = Filter()


class TestClass(unittest.TestCase):

    def testNotMatching(self):
        self.assertEqual("", pyfilter.parse("Hello"))
        self.assertEqual("", pyfilter.parse("HelloWorld"))
        self.assertEqual("", pyfilter.parse("Hello\nWorld"))
        self.assertEqual("", pyfilter.parse("Hello\nWorld\n"))
        self.assertEqual("", pyfilter.parse("\nHello\nWorld\n"))
        self.assertEqual("", pyfilter.parse("\n"))
        self.assertEqual("", pyfilter.parse(""))

    def testMatching(self):
        self.assertEqual("undefined reference to `Hello'\n",
                pyfilter.parse("../../File: 123: hashtagyolo: undefined reference to `Hello'"))
        self.assertEqual("undefined reference to hellothisisaverylongname yes indeed\n",
                pyfilter.parse("../../File: 123: hashtagyolo: undefined reference to hellothisisaverylongname yes indeed"))

    def testRemoveDuplicates(self):
        undef_a = "undefined reference to a\n"
        self.assertEqual(undef_a,
                pyfilter.parse(undef_a + undef_a))
        self.assertEqual(undef_a,
                pyfilter.parse(undef_a + undef_a + undef_a))


unittest.main()
