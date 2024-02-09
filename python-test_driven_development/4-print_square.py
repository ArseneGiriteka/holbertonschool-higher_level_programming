#!/usr/bin/python3
"""
The new module
"""


def print_square(size):
    """
    This is my function
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("#" * size)
