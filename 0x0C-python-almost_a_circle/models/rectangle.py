#!/usr/bin/python3
"""
module with a rectangle
"""

from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        self.id = id
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(self.id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter of width"""
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")

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
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """area method"""
        return self.__width * self.__height

    def display(self):
        """display rectangle with # char"""
        for i in range(self.__height):
            print("#" * self.__width)
