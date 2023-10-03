#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """test integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 30, 20, 5]), 30)
        self.assertEqual(max_integer([10, -2, 30, -7]), 30)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-10, 0, -8]), 0)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-2, -10, -80, -3]), -2)
