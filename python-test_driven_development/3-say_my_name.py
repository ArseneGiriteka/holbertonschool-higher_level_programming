#!/usr/bin/python3
"""
This is a new module
"""


def say_my_name(first_name, last_name=""):
    """
    This function tells you the real name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is{}{}".format(
        " " + first_name if first_name else "",
        " " + last_name if last_name else ""))
