#!/usr/bin/python3
""" This module contains a function that returns
    the peak of a list
"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    save = list_of_integers[1]
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and\
                list_of_integers[i] >= list_of_integers[i + 1]:
            save = list_of_integers[i]
    return save
