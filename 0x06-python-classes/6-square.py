#!/usr/bin/python3
"""sos tremendo, yulien jolverton"""


class Square:
    """square with conditions"""
    def __init__(self, size=0, position=(0, 0)):
        """init with the conditions for the attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position

    @property
    def size(self):
        """getter thing"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter thing"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, position):
        if len(position) != 2 and
        (type(position[0]) is not int and type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """print square"""
        x = self.__size
        if x > 0:
            for i in range(x):
                for j in range(x):
                    print("#", end="")
                print()
        else:
            print()

    def area(self):
        """method for returning area of square"""
        a = self.__size
        return a * a
