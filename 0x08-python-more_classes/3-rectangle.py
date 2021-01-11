#!/usr/bin/python3
"""
Module with a class for a rectangle
"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """init method"""
        self.__width = width
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """getter for width"""
        return self.__width
    @width.setter
    def width(self, width):
        """setter for width"""
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter for height"""
        return self.__height
    @height.setter
    def height(self, height):
        """setter for height"""
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """return the string"""
        rec = ""
        if self.__width is 0 or self.__height is 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                rec += "#"
            if i < (self.__height - 1):
                rec += "\n"
        return rec
