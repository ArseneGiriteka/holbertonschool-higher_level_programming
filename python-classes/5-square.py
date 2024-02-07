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
    Create a public getter of size attribute
    Greate a public setter of size attribute
    Create a public instance method my_print(self)
"""


class Square:
    """
    Note:
        This class represente a Square objects

    Attributes:
        size (int): private instance attribute

    Methods:
        area(self): a public instance method
        size(self): a public instance method
        size(self, size): a public instance method
        my_print(self): public instance method

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

    @property
    def size(self):
        """
        Note:
            This is a getter of size attribute

        Args:
            self(Square): square object

        Return:
            self.size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Note:
            This is the setter of self.size

        Args:
            self(Square): Square object
            size(int): value to set upon self.size

        Return:
            Nothing
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """
        Note:
            this method print self

        Args:
            self(Square): an object of type Square

        Return:
            Nothing
        """
        hashtag = "#"

        if self.size == 0:
            print()

        for i in range(0, self.size):
            print(hashtag * self.size)
