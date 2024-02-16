#!/usr/bin/python3
"""This is a module"""


class MyList(list):
    """This is MyList class"""

    def print_sorted(self):
        """Print_sorted method"""
        if self not None or is isinstance(self, None):
            print(sorted(self))
