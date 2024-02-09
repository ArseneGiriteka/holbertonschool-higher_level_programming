#!/usr/bin/python3
unittest = __import__('unittest')
max_integer = __import__('6-max_integer').max_integer
"""
This is a new module
"""


class TestMaxInteger(unittest.TestCase):
    """
    docstring for ClassName
    """
    def assertEqual(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 2, 4, 3]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([5, 5, 5, 5]), 0)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([0]), 0)
        with self.assertRaise(TypeError):
            max_integer()
        with self.assertRaise(TypeError):
            max_integer(["school", 5, 5, 5])
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([5.5, 56.87, 100.2, 87.3]), 100.2)
        self.assertEqual(max_integer([-5.5, -2.5, -3.8, -4.5]), -2.5)
        self.assertEqual(max_integer([5.5, 2, 3, 4]), 5.5)
        self.assertEqual(max_integer([5.58, -2, 3, -4]), 5.58)


if __name__ == "__main__":
    unittest.main()
