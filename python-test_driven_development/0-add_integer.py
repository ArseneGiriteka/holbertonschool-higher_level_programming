#!/usr/bin/python3
"""

This module contains add_integer function

"""


def add_integer(a, b=98):
    """
    This function add two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
