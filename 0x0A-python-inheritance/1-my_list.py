#!/usr/bin/python3
"""
dale nieri
"""


class MyList(list):
    """class that inherists from list class"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
