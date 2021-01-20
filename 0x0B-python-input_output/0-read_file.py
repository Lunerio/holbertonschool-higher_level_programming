#!/usr/bin/python3
"""this module contains a function
for reading a file
"""


def read_file(filename=""):
    """read a file and print each line"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
