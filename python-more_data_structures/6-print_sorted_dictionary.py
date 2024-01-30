#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    list(map(
        lambda key: print("{}: {}".format(key, a_dictionary[key])),
        sorted(a_dictionary.keys())
        )
        )
