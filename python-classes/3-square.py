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
    Create a public method called area(self)
"""


class Square:
    """
    Note:
        This class represente a Square objects

    Attributes:
        size (int): private instance attribute

    Methods:
        erea(self): a public instance method

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

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


    def area(self):
        """
        Note:
            This method compute the area of the Square object instance
            Return the area of the self object

        Args:
            self (Square): the Square instance

        Return:
            The Square of self
        """
        return self.__size * self.__size
