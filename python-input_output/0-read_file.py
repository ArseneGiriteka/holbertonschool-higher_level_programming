#!/usr/bin/python3
"""
This is a new module
"""


def read_file(filename=""):
    with open(filename) as _file:
        print(_file.read(), end="")
