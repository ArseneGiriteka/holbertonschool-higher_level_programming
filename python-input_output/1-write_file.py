#!/usr/bin/python3
"""
this is a method
"""


def write_file(filename="", text=""):
    """
    this is a method
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
