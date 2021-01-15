#!/usr/bin/python3
"""Unittest
for
max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """List of tests"""
    def test_ints(self):
        """test with a list of ints"""
        self.assertEqual(max_integer([1, 2, 8, 4]), 8)

    def test_empty(self):
        """test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_char(self):
        """test a list of chars(ASCII)"""
        self.assertEqual(max_integer(["a", "C", "c", "b"]), "c")

    def test_not_list(self):
        """testing int as argument"""
        with self.assertRaises(TypeError):
            max_integer(13)

    def test_none(self):
        """testing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def first_one(self):
        """testing the max at the beginning"""
        self.assertEqual(max_integer([28, 2, 3, 6]), 28)

    def las_one(self):
        """testing the max at the end"""
        self.assertEqual(max_integer([3, 2, 5, 35]), 35)

    def one_element(self):
        """testing a list of one element"""
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
