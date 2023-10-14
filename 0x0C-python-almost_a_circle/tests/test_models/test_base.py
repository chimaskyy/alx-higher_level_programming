#!/usr/bin/python3
"""
Unittest for class Base
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        """
        counter setUp
        """
        Base._Base__nb_objects = 0

    def test_Base_without_argument(self):
    
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_Base_with_argument(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_Base_with_without_argument(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(5)
        b4 = Base()
        self.assertEqual(b4.id, 3)
    
    def test_Base_with_bool(self):
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_Base_with_negnum(self):
        b1 = Base(-6)
        self.assertEqual(b1.id, -6)



