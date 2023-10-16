#!/usr/bin/python3
"""
Unittest for class Base
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



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

    
    '''def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")'''

    def test_to_json_string_no_args(self):
        """no arg"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        _type = type(Base.to_json_string([r.to_dictionary()]))
        self.assertEqual(_type, str)

    def test_to_json_string_type(self):
        r = Square(10, 7, 2, 8)
        _type = type(Base.to_json_string([r.to_dictionary()]))
        self.assertEqual(_type, str)

    def test_save_to_file_with_obj(self):
        r1 = Rectangle(1, 4, 5, 7, 8)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertTrue(content)
            self.assertTrue(len(content) == 52)
            self.assertTrue(type(content), str)

    '''def test_save_to_file_None(self):
        self.assertEqual(Rectangle.save_to_file(None), [])

    def test_save_to_file_empty(self):
        self.assertEqual(Rectangle.save_to_file([]), [])'''
    
    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_args(self):
        '''wrong arg'''
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(4)

    def test_save_to_file_args(self):
        '''test more than one arg'''
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([2], [5])
    
    def test_save_to_file_with_obj(self):
        r1 = Square(1, 4, 7, 8)
        Square.save_to_file([r1])

        with open("Square.json", "r") as f:
            content = f.read()
            self.assertTrue(content)
            self.assertTrue(len(content) == 38)
            self.assertTrue(type(content), str)

    '''def test_save_to_file_empty(self):
        self.assertEqual(Base.save_to_file([]), [])

    def test_save_to_file_None(self):
        self.assertEqual(Base.save_to_file(None), [])'''

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))
        self.assertEqual(str, type(json_list_input))

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4},
                      {"id": 4, "width": 5, "height": 9}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))
        self.assertEqual(str, type(json_list_input))

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_load_from_file_Error(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_load_from_file_Error(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()



