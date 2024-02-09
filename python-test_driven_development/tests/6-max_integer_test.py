#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test max_integer with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_sorted_list(self):
        """Test max_integer with a reverse sorted list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test max_integer with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list containing mixed positive
        and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element_list(self):
        """Test max_integer with a list containing a single element"""
        self.assertEqual(max_integer([4]), 4)

    def test_duplicate_max_values(self):
        """Test max_integer with a list containing duplicate maximum values"""
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
