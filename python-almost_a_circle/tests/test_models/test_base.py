#!/usr/bin/python3
"""New module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class methods"""

    def setUp(self):
        """Set up for testing."""
        Base._Base__nb_objects = 0

    def test_auto_id_assignment_exists(self):
        """Test of Base() for assigning automatically
        an ID exists."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_auto_id_increment_exists(self):
        """Test of Base() for assigning automatically
        an ID + 1 of the previous exists."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_auto_assign_id_plus_one_exists(self):
        """Test Base() for assigning automatically
        an ID + 1 of the previous exists."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_passed_exists(self):
        """Test Base(89) saving the ID passed exists."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none_exists(self):
        """Test Base.to_json_string(None) exists."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list_exists(self):
        """Test Base.to_json_string([]) exists."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_dict_exists(self):
        """Test Base.to_json_string([ { 'id': 12 }]) exists."""
        self.assertEqual(
                    Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_returns_string_exists(self):
        """Test Base.to_json_string([ { 'id': 12 }]) returning a string
        exists."""
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_string_none_exists(self):
        """Test Base.from_json_string(None) exists."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string_exists(self):
        """Test Base.from_json_string("[]") exists."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_dict_exists(self):
        """Test Base.from_json_string('[{ "id": 89 }]') exists."""
        self.assertEqual(
                    Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

    def test_from_json_string_returns_list_exists(self):
        """Test Base.from_json_string('[{ "id": 89 }]') returning a
        list exists."""
        self.assertIsInstance(
                    Base.from_json_string('[{ "id": 89 }]'), list)

    def tearDown(self):
        """Tear down after testing."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
