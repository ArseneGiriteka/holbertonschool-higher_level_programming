#!/usr/bin/python3
"""this is a new module"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """this is a method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This is a method"""
        return self.width

    @size.setter
    def size(self, size):
        """This is a method"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the attributes of the Square."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return string representation of Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}
