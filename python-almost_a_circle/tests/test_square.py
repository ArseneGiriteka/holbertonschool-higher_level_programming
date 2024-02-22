#!/usr/bin/python3
"""this is a module"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        s1 = Square(10)
        self.assertEqual(s1.size, 10)

    def test_area(self):
        s1 = Square(10)
        self.assertEqual(s1.area(), 100)

    def test_display(self):
        s1 = Square(3)
        self.assertEqual(s1.display(), "###\n###\n###\n")

    def test_str(self):
        s1 = Square(10)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")

    def test_update(self):
        s1 = Square(10)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test_to_dictionary(self):
        s1 = Square(10)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 10, 'x': 0, 'y': 0})


if __name__ == '__main__':
    unittest.main()