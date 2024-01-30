#!/usr/bin/pyhon3


def update_dictionary(a_dictionary, key, value):
    if isinstance(key, str):
        a_dictionary[key] = value
        a_dictionary.update()
    return a_dictionary
