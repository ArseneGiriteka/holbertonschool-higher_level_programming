#!/usr/bin/python3
"""this is a module"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """This is a Square Rectangle"""
 

    def __init__(self, size):
        """this is a method"""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area method"""
        return self.__size ** 2 
