#!/usr/bin/python3
"""
This module define a class called Square
Attributes:
    size (int): it represente the size of a side of
    the square object

Todo:
    define class Square
    define a private instance attribute calle "size"
    raise TypeError if size isn't integer
    raise ValueError if size is less that zero
"""


class Square:
    """
    Note:
        This class represente a Square objects

    Attributes:
        size (int) : private instance attribute

    Args:
        size (int)
    """
    def __init__(self, size=0):
        """
        Note:
            This methode initialize a square object
            It raises TypeError if size is not integer
            It raises ValueError if size < 0

        Args:
            self (Square): private square instance object
            size (int): square object one side size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
