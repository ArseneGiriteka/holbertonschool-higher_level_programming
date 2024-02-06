#!/usr/bin/python3
"""
This module define a class called Square
Attributes:
    size (int): it represente the size of a side of
    the square object

Todo:
    define class Square
    define a private instance attribute calle "size"
"""


class Square:
    """
    Note:
        This class represente a Square object

    Attributes:
        size (int) : private instance attribute

    Args:
        size (int)
    """
    def __init__(self, size):
        """
        Note:
            This methode initialize a square object

        Args:
            self (Square): private square instance object
            size (int): square object one side size
        """
        self.__size = size
