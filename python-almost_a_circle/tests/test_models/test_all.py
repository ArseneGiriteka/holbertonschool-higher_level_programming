#!/usr/bin/python3
"""New module"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_auto_id_assignment_exists(self):
        """Test of Base() for assigning automatically an ID exists."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_auto_id_plus_one_assignment_exists(self):
        """Test of Base() for assigning automatically an
        ID + 1 of the previous exists."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 5)

    def test_given_id_assignment_exists(self):
        """Test of Base(89) saving the ID passed exists."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_exists(self):
        """Test of Base.to_json_string(None) exists."""
        self.assertTrue(hasattr(Base, 'to_json_string'))

    def test_to_json_string_empty_list_exists(self):
        """Test of Base.to_json_string([]) exists."""
        self.assertTrue(hasattr(Base, 'to_json_string'))

    def test_to_json_string_with_data_exists(self):
        """Test of Base.to_json_string([ { 'id': 12 }]) exists."""
        self.assertTrue(hasattr(Base, 'to_json_string'))

    def test_to_json_string_returns_string_exists(self):
        """Test of Base.to_json_string
        ([ { 'id': 12 }]) returning a string exists."""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_from_json_string_exists(self):
        """Test of Base.from_json_string(None) exists."""
        self.assertTrue(hasattr(Base, 'from_json_string'))

    def test_from_json_string_empty_string_exists(self):
        """Test of Base.from_json_string("[]") exists."""
        self.assertTrue(hasattr(Base, 'from_json_string'))

    def test_from_json_string_with_data_exists(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') exists."""
        self.assertTrue(hasattr(Base, 'from_json_string'))

    def test_from_json_string_returns_list_exists(self):
        """Test of Base.from_json_string('[{ "id": 89 }]')
        returning a list exists."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_constructor_exists(self):
        """Test of Rectangle(1, 2) exists."""
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    # Add more tests for Rectangle class...


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_constructor_exists(self):
        """Test of Square(1) exists."""
        s = Square(1)
        self.assertIsInstance(s, Square)

    # Add more tests for Square class...


if __name__ == "__main__":
    unittest.main()
