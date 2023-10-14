#!/usr/bin/python3
"""
Unittest for class Base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Testing Rectangle class"""
    def setUp(self):
        '''counter setUp'''
        
        Base._Base__nb_objects = 0

    def test_rect_id(self):
        """Retrieve Rectangle id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 5)
        self.assertEqual(r2.id, 2)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(3)
    
    def test_three_args(self):
        r1 = Rectangle(5, 6, 7)
        self.assertEqual(r1.id, 1)

    def test_four_args(self):
        r1 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, 1)
    
    def test_all_argument(self):
        r1 = Rectangle(5, 6, 8, 9, 9)
        self.assertEqual(r1.id, 9)


    def test_width_private_attr(self):
        """Test width as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__width"))

    def test_height_private_attr(self):
        """Test height as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__height"))

    def test_x_private_attr(self):
        """Test x as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__x"))

    def test_y_private_attr(self):
        """Test y as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__y"))

    def test_getter_width(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        self.assertEqual(r1.width, 7)

    def test_setter_width(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        r1.width = 30
        self.assertEqual(r1.width, 30)

    def test_getter_height(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        self.assertEqual(r1.height, 8)

    def test_setter_width(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        r1.height = 30
        self.assertEqual(r1.height, 30)

    def test_getter_x(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        self.assertEqual(r1.x, 9)

    def test_setter_x(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        r1.x = 30
        self.assertEqual(r1.x, 30)

    def test_getter_y(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        self.assertEqual(r1.y, 0)

    def test_setter_y(self):
        r1 = Rectangle(7, 8, 9, 0, 5)
        r1.y = 30
        self.assertEqual(r1.y, 30)

    def test_Error_width(self):
        '''Test for ivalid attribute(value) for width'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(True, 5)
        
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(None, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle(0.5, 5)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1 = Rectangle(-8, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle((1,2), 5)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1 = Rectangle(0, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle({1: 4}, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle("8", 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle([1, 3], 5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_Error_height(self):
        '''Test for ivalid attribute(value) for height'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(5, True)
        
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(5, None)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(5, 0.5)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r1 = Rectangle(8, -5)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(4, (5, 6))

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r1 = Rectangle(5, 0)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(6,{1, 5})

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(8, "5")

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1 = Rectangle(1, [5, 7])

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('nan'))

    def test_Error_x(self):
        '''Test for ivalid attribute(value) for height'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(5, 5, "8")
        
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(5, 6, [5,7])

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1 = Rectangle(5, 5, (4, 6))

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r1 = Rectangle(8, 8, -5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 6, float('inf'))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 5, float('nan'))

    def test_Error_y(self):
        '''Test for ivalid attribute(value) for height'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(5, 5, 7, "8")
        
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(5, 6, 7, [5,7])

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1 = Rectangle(5, 5, 6, (4, 6))

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r1 = Rectangle(8, 8, 5, -5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 8, float('inf'))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 5, 0, float('nan'))

    def test_area(self):
        r1 = Rectangle(5, 5)
        self.assertEqual(r1.area(), 25)

    def test_area(self):
        r1 = Rectangle(5, 2, 0, 0, 4)
        self.assertEqual(r1.area(), 10)

    def test_area(self):
        r1 = Rectangle(5, 2, 0, 0, 4)
        r1.width = 3
        r1.height = 3
        self.assertEqual(r1.area(), 9)