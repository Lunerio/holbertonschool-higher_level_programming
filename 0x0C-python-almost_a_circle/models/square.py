#!/usr/bin/python3
"""module for the class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))
