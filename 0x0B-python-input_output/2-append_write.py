#!/usr/bin/python3
"""module with an append function"""


def append_write(filename="", text=""):
    """write text into filename"""
    with open(filename, 'a') as f:
        f.write(text)
    return (len(text))
