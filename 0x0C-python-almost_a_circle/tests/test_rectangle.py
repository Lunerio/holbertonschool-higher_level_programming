#!/usr/bin/python3
"""test module for rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """testing the Rectangle class and its methods"""

    def test_inst_methods(self):
        """test methods"""
        test_inst = Rectangle(2, 3, 0, 0, 1)
        """test area of rectangle"""
        self.assertEqual(test_inst.area(), 6)
        """test str"""
        self.assertEqual(test_inst.__str__(), '[Rectangle] (1) 0/0 - 2/3')
        """test to_dictionary"""
        self.assertEqual(test_inst.to_dictionary(),
                         {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0})

    def test_negatives(self):
        """test negative values"""
        with self.assertRaises(ValueError):
            """negative width"""
            fail_inst = Rectangle(-2, 3, 3, 0, 0)
        with self.assertRaises(ValueError):
            """negative height"""
            fail_inst = Rectangle(2, -3, 3, 0, 0)
        with self.assertRaises(ValueError):
            """negative x"""
            fail_inst = Rectangle(2, 3, -1, 0, 0)
        with self.assertRaises(ValueError):
            """negative y"""
            fail_inst = Rectangle(-2, 3, 0, -2, 0)

    def test_not_int(self):
        """test values without ints"""
        with self.assertRaises(TypeError):
            """on width"""
            fail_inst = Rectangle('testStr', 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            """on height"""
            fail_inst = Rectangle(3, '3', 0, 0, 1)
        with self.assertRaises(TypeError):
            """on x"""
            fail_inst = Rectangle(1, 3, '0', 0, 1)
        with self.assertRaises(TypeError):
            """on y"""
            fail_inst = Rectangle(2, 3, 0, '0', 1)

    def test_None_values(self):
        """test None values"""
        with self.assertRaises(TypeError):
            """on width"""
            fail_inst = Rectangle(None, 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            """on height"""
            fail_inst = Rectangle(2, None, 0, 0, 1)
        with self.assertRaises(TypeError):
            """on x"""
            fail_inst = Rectangle(2, 3, None, 0, 1)
        with self.assertRaises(TypeError):
            """on y"""
            fail_inst = Rectangle(2, 5, 0, None, 1)

if __name__ == '__main__':
    unittest.main()
