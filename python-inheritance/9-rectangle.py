#!/usr/bin/python3
"""This is a module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """This is a class"""
    
    def __init__(self, width, height):
        """this is a method"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
