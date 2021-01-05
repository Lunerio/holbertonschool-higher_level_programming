#!/usr/bin/python3
"""Dejate de joder"""


class Square:
    """ Class Square with constuctor method"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculate the area of a square"""
        x = self.__size
        return x * x

    def my_print(self):
        """Print the square checking position"""
        x = self.__size
        if x == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(x):
                print(" " * self.__position[0], end="")
                for i in range(x):
                    print("#", end="")
                print()

    @property
    def position(self):
        """getter function of position"""
        return self.__position

    @position.setter
    def position(self, position):
        """setter for position"""
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """getter function of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter function of attribute size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
