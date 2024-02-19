#!/usr/bin/python3
"""
This is a module
"""
import json


def load_from_json_file(filename):
    """
    This is a method
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
