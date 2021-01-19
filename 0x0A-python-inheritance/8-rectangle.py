#!/usr/bin/python3
"""
This module contains a class called BaseGeometry"""


class BaseGeometry():
    """contains a method"""
    def area(self):
        """raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry
    Validates height and width with
    integer_validator
    """
    def __init__(self, width, height):
        """initializer"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
