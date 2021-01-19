#!/usr/bin/python3
"""
This module contains a class called BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry
    Validates height and width with
    integer_validator
    """
    def __init__(self, width, height):
        """initializer"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def __str__(self):
        """print given string"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        "return area of rectangle"
        return (self.__width * self.__height)
