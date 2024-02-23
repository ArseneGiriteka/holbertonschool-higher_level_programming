#!/usr/bin/python3
"""New module"""


import unittest
import io
import os
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_constructor_exists(self):
        """Test Rectangle(1, 2) exists."""
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    def test_constructor_with_x_and_y_exists(self):
        """Test Rectangle(1, 2, 3) exists."""
        r = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r, Rectangle)

    def test_width_property_exists(self):
        """Test Rectangle.width property exists."""
        r = Rectangle(5, 2)
        self.assertEqual(r.width, 5)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_setter_exists(self):
        """Test Rectangle.width setter exists."""
        r = Rectangle(5, 2)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_negative_values(self):
        # Test constructor with negative width
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        
        # Test constructor with negative height
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        
        # Test constructor with zero width
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        
        # Test constructor with zero height
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        
        # Test constructor with negative x coordinate
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        
        # Test constructor with negative y coordinate
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
    
    def test_area(self):
        # Test area calculation
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_width_setter_invalid_value(self):
        """Test Rectangle.width setter with invalid value."""
        r = Rectangle(5, 2)
        with self.assertRaises(ValueError):
            r.width = -5

    def test_update_exists(self):
        """Test Rectangle.update() exists."""
        r = Rectangle(5, 2)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(str(r), "[Rectangle] (10) 40/50 - 20/30")

    def test_str_exists(self):
        """Test __str__() for Rectangle exists."""
        r = Rectangle(5, 2, 3, 4, 45)
        self.assertEqual(str(r), "[Rectangle] (45) 3/4 - 5/2")

    def test_to_dictionary_exists(self):
        """Test to_dictionary() in Rectangle exists."""
        r = Rectangle(5, 2, 3, 4, 45)
        self.assertEqual(
                    r.to_dictionary(),
                    {'id': 45, 'x': 3, 'y': 4, 'width': 5, 'height': 2})

    def test_display_with_x_and_y(self):
        # Test display with both x and y
        rect = Rectangle(3, 4, 2, 1)
        expected_output = "\n  ###\n  ###\n  ###\n  ###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            rect.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display_with_x_only(self):
        # Test display with only x
        rect = Rectangle(3, 4, 2)
        expected_output = "  ###\n  ###\n  ###\n  ###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            rect.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display_without_x_and_y(self):
        # Test display without x and y
        rect = Rectangle(3, 4)
        expected_output = "###\n###\n###\n###\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            rect.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_rectangle_create_with_id(self):
        # Test Rectangle.create() with id
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual(rect.id, 89)

    def test_rectangle_create_with_id_and_width(self):
        # Test Rectangle.create() with id and width
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_create_with_id_width_and_height(self):
        # Test Rectangle.create() with id, width, and height
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_create_with_id_width_height_and_coordinates(self):
        # Test Rectangle.create() with id, width, height, and coordinates
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_save_to_file_none(self):
        # Test Rectangle.save_to_file() with None
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_rectangle_save_to_file_empty_list(self):
        # Test Rectangle.save_to_file() with an empty list
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_rectangle_save_to_file_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_rectangle_save_to_file_single_rectangle(self):
        # Create an instance of Rectangle for testing
        rect = Rectangle(1, 2, 3, 4, 99)
        
        # Save the Rectangle instance to file
        Rectangle.save_to_file([rect])
        
        # Check if the file exists
        self.assertTrue(os.path.exists("Rectangle.json"))

        # Check if the file content matches the expected JSON string
        with open("Rectangle.json", "r") as file:
            expected_output = '[{"id": 99, "x": 3, "y": 4, "width": 1, "height": 2}]'
            self.assertEqual(file.read(), expected_output)

    def test_rectangle_load_from_file_existing_file(self):
        # Test Rectangle.load_from_file() when the file exists
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        self.assertEqual(rects[0].id, 1)
        self.assertEqual(rects[0].width, 1)
        self.assertEqual(rects[0].height, 2)
        self.assertEqual(rects[0].x, 0)
        self.assertEqual(rects[0].y, 0)

    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None) in Rectangle exists."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()
