#!/usr/bin/python3
"""
This is Rectangle class module
"""


class Rectangle:
    """
    This is a Rectangle class definition
    """

    def __init__(self, width=0, height=0):
        """
        This is __init__ method
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Compute the area"""
        return self.__width * self.__height

    def perimeter(self):
        """compute the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """return string"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(0, self.__height - 1):
            string += '#' * self.__width + '\n'
        string += '#' * self.__width
        return string

    def __repr__(self):
        """__repr__ function"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """destructor"""
        print("Bye rectangle...")
