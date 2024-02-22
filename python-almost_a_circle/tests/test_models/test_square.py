import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_constructor_exists(self):
        """Test Square(1) exists."""
        s = Square(1)
        self.assertIsInstance(s, Square)

    def test_constructor_with_x_and_y_exists(self):
        """Test Square(1, 2) exists."""
        s = Square(1, 2, 3)
        self.assertIsInstance(s, Square)

    def test_size_property_exists(self):
        """Test Square.size property exists."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter_exists(self):
        """Test Square.size setter exists."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_size_setter_invalid_value(self):
        """Test Square.size setter with invalid value."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -5

    def test_update_exists(self):
        """Test Square.update() exists."""
        s = Square(5)
        s.update(10, 20, 30, 40)
        self.assertEqual(str(s), "[Square] (10) 30/40 - 20")

    def test_str_exists(self):
        """Test __str__() for Square exists."""
        s = Square(5, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 5")

    def test_to_dictionary_exists(self):
        """Test to_dictionary() in Square exists."""
        s = Square(5, 2, 3, 4)
        self.assertEqual(s.to_dictionary(), {'id': 4, 'size': 5, 'x': 2, 'y': 3})


if __name__ == "__main__":
    unittest.main()
