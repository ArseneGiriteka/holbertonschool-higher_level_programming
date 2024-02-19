#!/usr/bin/python3
"""
This is a module
"""


def append_write(filename="", text=""):
    """
    This a method
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
