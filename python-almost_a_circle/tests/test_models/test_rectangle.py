import unittest
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

    def test_width_setter_exists(self):
        """Test Rectangle.width setter exists."""
        r = Rectangle(5, 2)
        r.width = 10
        self.assertEqual(r.width, 10)

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
        self.assertEqual(r.to_dictionary(), {'id': 45, 'x': 3, 'y': 4, 'width': 5, 'height': 2})


if __name__ == "__main__":
    unittest.main()
