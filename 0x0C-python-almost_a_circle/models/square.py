#!/usr/bin/python3
"""module for the class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method for new values"""
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            values_list = ['id', 'size', 'x', 'y']
            if len(args) > 4:
                raise TypeError("4 values max")

            for i in range(len(args)):
                setattr(self, values_list[i], args[i])

    def to_dictionary(self):
        """return dictionary with values"""
        values_dict = {'id': self.id, 'size': self.width,
                       'x': self.x, 'y': self.y}
        return values_dict
