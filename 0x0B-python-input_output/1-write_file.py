#!/usr/bin/python3
"""module with a write function"""


def write_file(filename="", text=""):
    """write text into filename"""
    with open(filename, 'w') as f:
        f.write(text)
    return (len(text))
