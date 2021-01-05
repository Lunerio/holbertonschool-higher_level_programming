#!/usr/bin/python3
"""sos tremendo, yulien jolverton"""


class Square:
    """square with conditions"""
    def __init__(self, size=0):
        """init with the conditions for the attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """getter thing"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter thing"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """method for returning area of square"""
        a = self.__size
        return a * a
