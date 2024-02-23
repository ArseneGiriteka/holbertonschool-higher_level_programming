#!/usr/bin/python3
"""New module"""


import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_constructor_exists(self):
        """Test Square(1) exists."""
        s = Square(1)
        self.assertIsInstance(s, Square)

    def test_square_constructor_exists(self):
        """Test Square(1, 2) exists."""
        square = Square(1, 2)
        self.assertIsInstance(square, Square)

    def test_square_constructor_with_x_and_y_exists(self):
        """Test Square(1, 2, 3) exists."""
        square = Square(1, 2, 3)
        self.assertIsInstance(square, Square)

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
        self.assertEqual(
                    s.to_dictionary(), {'id': 4, 'size': 5, 'x': 2, 'y': 3})

    def test_constructor_with_width_and_height_exists(self):
        """Test Square(1, 2) exists."""
        s = Square(1, 2)
        self.assertIsInstance(s, Square)

    def test_constructor_with_width_height_and_coordinates_exists(self):
        """Test Square(1, 2, 3) exists."""
        s = Square(1, 2, 3)
        self.assertIsInstance(s, Square)

    def test_constructor_with_string_width_exists(self):
        """Test Square("1") exists."""
        with self.assertRaises(TypeError):
            s = Square("1")
            self.assertIsInstance(s, Square)

    def test_constructor_with_string_height_exists(self):
        """Test Square(1, "2") exists."""
        with self.assertRaises(TypeError):
            s = Square(1, "2")
            self.assertIsInstance(s, Square)

    def test_constructor_with_string_coordinates_exists(self):
        """Test Square(1, 2, "3") exists."""
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")
            self.assertIsInstance(s, Square)

    def test_constructor_with_negative_size_exists(self):
        """Test Square(-1) exists."""
        with self.assertRaises(ValueError):
            s = Square(-1)
            self.assertIsInstance(s, Square)

    def test_constructor_with_width_and_negative_height_exists(self):
        """Test Square(1, -2) exists."""
        with self.assertRaises(ValueError):
            s = Square(1, -2)
            self.assertIsInstance(s, Square)

    def test_constructor_with_width_height_and_negative_coordinates_exists(self):
        """Test Square(1, 2, -3) exists."""
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)
            self.assertIsInstance(s, Square)

    def test_constructor_with_zero_size_exists(self):
        """Test Square(0) exists."""
        with self.assertRaises(ValueError):
            s = Square(0)
            self.assertIsInstance(s, Square)

    def test_square_create_with_id(self):
        # Test Square.create() with id
        square = Square.create(**{'id': 89})
        self.assertEqual(square.id, 89)

    def test_square_create_with_id_and_size(self):
        # Test Square.create() with id and size
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_square_create_with_id_size_and_x(self):
        # Test Square.create() with id, size, and x
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_square_create_with_id_size_x_and_y(self):
        # Test Square.create() with id, size, x, and y
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_save_to_file_none(self):
        # Test Square.save_to_file() with None
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_empty_list(self):
        # Test Square.save_to_file() with an empty list
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_single_square(self):
        # Create an instance of Square for testing
        square = Square(1, 2, 3, 4)
        
        # Save the Square instance to file
        Square.save_to_file([square])
        
        # Check if the file exists
        self.assertTrue(os.path.exists("Square.json"))

        # Check if the file content matches the expected JSON string
        with open("Square.json", "r") as file:
            expected_output = '[{"id": 4, "size": 1, "x": 2, "y": 3}]'
            self.assertEqual(file.read(), expected_output)

    def test_square_load_from_file_existing_file(self):
        # Test Square.load_from_file() when the file exists
        with open("Square.json", "w") as file:
            file.write('[{"id": 1, "size": 1, "x": 0, "y": 0}]')
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0].id, 1)
        self.assertEqual(squares[0].size, 1)
        self.assertEqual(squares[0].x, 0)
        self.assertEqual(squares[0].y, 0)

    def test_square_save_to_file_none(self):
        """Test Square.save_to_file(None) exists."""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == "__main__":
    unittest.main()
