#!/usr/bin/python3
"""module for the class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """string method"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = self.size
        self.__height = self.size
