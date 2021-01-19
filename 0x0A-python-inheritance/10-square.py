#!/usr/bin/python3
"""
This module contains a class called BaseGeometry"""


class BaseGeometry():
    """contains a method"""
    def area(self):
        """return area of rectangle"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator for value"""
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
