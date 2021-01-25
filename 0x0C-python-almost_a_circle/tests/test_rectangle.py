#!/usr/bin/python3
"""test module for rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """testing the Rectangle class and its methods"""

    def test_inst_methods(self):
        test_inst = Rectangle(2, 3, 0, 0, 1)
        """test area of rectangle"""
        self.assertEqual(test_inst.area(), 6)
        """test str"""
        self.assertEqual(test_inst.__str__(), '[Rectangle] (1) 0/0 - 2/3')
        """test to_dictionary"""
        self.assertEqual(test_inst.to_dictionary(),
                         {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0})
        """test display"""
        self.assertMultiLineEqual(test_inst.display(), '##\n##\n##\n')


if __name__ == '__main__':
    unittest.main()
