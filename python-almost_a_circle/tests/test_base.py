#!/usr/bin/python3
"""this is a python module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base(-7)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, -7)

    def test_to_json_string(self):
        pass  # Add tests for to_json_string method

    def test_from_json_string(self):
        pass  # Add tests for from_json_string method

    def test_create(self):
        pass  # Add tests for create method

    def test_load_from_file(self):
        pass  # Add tests for load_from_file method


if __name__ == '__main__':
    unittest.main()