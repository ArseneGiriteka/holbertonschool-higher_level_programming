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
    def __init__(self, size=0, position=(0, 0)):
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

        if position is None or not isinstance(position, tuple) or\
                len(position) != 2 or\
                not isinstance(position[0], int) or\
                not isinstance(position[1], int) or\
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """
        Note:
            this is a position getter function

        Args:
            self(Square): an object of type square

        Return:
            (int, int): a two integer tuple represanting position
         """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Note:
            This is a position setter function

        Args:
            self(square): an object of type square
            position(int, int): 2D position

        Return:
            Nothing
        """
        if position is None or not isinstance(position, tuple) or\
                not len(position) != 2 or\
                not isinstance(position[0], int) or\
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
        underscore = "_"

        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(0, self.size):
                print(underscore * self.position[0], end="")
                print(hashtag * self.size)
