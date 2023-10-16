#!/usr/bin/python3
"""
Unitest for Square class
It inherited from Rectangle class
"""

import unittest
import sys
from io import StringIO
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Square class tests"""

    def setUp(self):
        '''counter setUp'''

        Base._Base__nb_objects = 0

    def test_square(self):
        sq_obj = Square(5)
        self.assertEqual(sq_obj.width, 5)
        self.assertEqual(sq_obj.id, 1)
        self.assertEqual(sq_obj.x, 0)
        self.assertEqual(sq_obj.height, 5)
        self.assertEqual(sq_obj.y, 0)

    def test_square(self):
        """test two args"""
        sq_obj = Square(5, 4)
        self.assertEqual(sq_obj.width, 5)
        self.assertEqual(sq_obj.id, 1)
        self.assertEqual(sq_obj.x, 4)
        self.assertEqual(sq_obj.height, 5)
        self.assertEqual(sq_obj.y, 0)

    def test_square(self):
        """test three args"""
        sq_obj = Square(5, 4, 6)
        self.assertEqual(sq_obj.width, 5)
        self.assertEqual(sq_obj.id, 1)
        self.assertEqual(sq_obj.x, 4)
        self.assertEqual(sq_obj.height, 5)
        self.assertEqual(sq_obj.y, 6)

    def test_square(self):
        """test four args"""
        sq_obj = Square(5, 6, 7, 3)
        self.assertEqual(sq_obj.width, 5)
        self.assertEqual(sq_obj.id, 3)
        self.assertEqual(sq_obj.x, 6)
        self.assertEqual(sq_obj.height, 5)
        self.assertEqual(sq_obj.y, 7)

    def test_error(self):
        """test type and value error"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Square([5], 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Square({5}, 6)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Square("5", 6, 5)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1 = Square(-6)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1 = Square(0)

    def test_str_print(self):
        """test str"""
        r = Square(4)
        expected = "[Square] (1) 0/0 - 4"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_str_print(self):
        """test str"""
        r = Square(4, 7)
        expected = "[Square] (1) 7/0 - 4"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_str_print(self):
        """test str"""
        r = Square(4, 4, 6)
        expected = "[Square] (1) 4/6 - 4"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_str_print(self):
        """test str"""
        r = Square(4, 3, 5)
        expected = "[Square] (1) 3/5 - 4"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_area(self):
        r1 = Square(5)
        self.assertEqual(r1.area(), 25)

    def test_getter_size(self):
        r1 = Square(7, 8, 9, 0)
        self.assertEqual(r1.size, 7)

    def test_setter_size(self):
        r1 = Square(7, 8, 9, 5)
        r1.size = 30
        self.assertEqual(r1.size, 30)

    def test_Square_update_args(self):
        '''test printing  updated rectangle'''
        r = Square(10, 10, 10, 10)
        r.update()
        r.update(4)
        r.update(4, 5)
        r.update(4, 5, 6)
        r.update(4, 5, 6, 7)

        expected = "[Square] (4) 6/7 - 5"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_RectangleUpdate_kwargs(self):
        '''change size'''
        r = Square(10, 10, 10, 10)
        r.update(size=4)
        expected = "[Square] (10) 10/10 - 4"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_RectangleUpdate_kwargs(self):
        '''change id'''
        r = Square(10, 10, 10, 10)
        r.update(id=4)
        expected = "[Square] (4) 10/10 - 10"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_RectangleUpdate_kwargs(self):
        '''change x'''
        r = Square(10, 10, 10, 10)
        r.update(x=4)
        expected = "[Square] (10) 4/10 - 10"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_RectangleUpdate_kwargs(self):
        '''change y'''
        r = Square(10, 10, 10, 10)
        r.update(y=4)
        expected = "[Square] (10) 10/4 - 10"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_RectangleUpdate_kwargs(self):
        '''change all args'''
        r = Square(10, 10, 10, 10)
        r.update(size=8, x=9, id=6, y=5)
        expected = "[Square] (6) 9/5 - 8"
        str_out = str(r)
        self.assertEqual(str_out, expected)

    def test_to_dictionary(self):
        r = Square(10, 5, 7)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict.get("id"), 1)
        self.assertEqual(r_dict.get("size"), 10)
        self.assertEqual(r_dict.get("x"), 5)
        self.assertEqual(r_dict.get("y"), 7)
