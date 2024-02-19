#!/usr/bin/python3
"""
This is a module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    this is a method
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
