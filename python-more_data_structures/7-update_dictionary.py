#!/usr/bin/pyhon3


def update_dictionary(a_dictionary, key, value):
    if isinstance(key, str):
        a_dictionary.update({"{}".format(key): value})
    return a_dictionary
