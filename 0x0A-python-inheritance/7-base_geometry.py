#!/usr/bin/python3
"""
This module contains a class called BaseGeometry
"""


class BaseGeometry():
    """contains a method"""
    def area(self):
        """raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator thing"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(name) != str:
            raise TypeError("name must be a string")
