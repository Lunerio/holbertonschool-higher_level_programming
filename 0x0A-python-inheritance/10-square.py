#!/usr/bin/python3
"""
This module contains a class called BaseGeometry"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """subclass of Rectangle"""
    def __init__(self, size):
        """instantiation"""
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """ return area of square"""
        return (self.__size * self.__size)
