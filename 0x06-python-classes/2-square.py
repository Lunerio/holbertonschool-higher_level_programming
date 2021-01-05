#!/usr/bin/python3
class Square:
    """square with conditions"""
    def __init__(self, size=0):
        """init with the conditions for the attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
