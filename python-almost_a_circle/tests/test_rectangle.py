#!/usr/bin/python3
"""This is a module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)

    def test_area(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

    def test_display(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.display(), "###\n###\n")

    def test_str(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 10/20")

    def test_update(self):
        r1 = Rectangle(10, 20)
        r1.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (1) 4/5 - 2/3")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.to_dictionary(), {'id': 1, 'width': 10,
        	    'height': 20, 'x': 0, 'y': 0})

if __name__ == '__main__':
    unittest.main()