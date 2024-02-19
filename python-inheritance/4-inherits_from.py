#!/usr/bin/python3
"""
This a module

this module check if an object inherits from some thye of an object

Methods:
    def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class
    that inherited (directly or indirectly)
    from the specified class a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
