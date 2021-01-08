#!/usr/bin/python3
"""
This module contains the add function
That returns an integer from the sum of a and b.
If a or b are not int or float raise TypeError.
"""


def add_integer(a, b=98):
    """
    check a or b for type. Return sum if valid
    """


    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is bool:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(b) is bool:
        raise TypeError("b must be an integer")

    # Cast a and b into int
    a = int(a)
    b = int(b)

    if a+1 == a:
        raise OverflowError
    if b+1 == b:
        raise OverflowError

    return a + b
