#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    _keys = [key for key, val in a_dictionary.items() if val == value]

    for key in _keys:
        del a_dictionary[key]

    return a_dictionary
