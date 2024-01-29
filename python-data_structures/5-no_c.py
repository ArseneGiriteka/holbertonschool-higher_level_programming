#!/usr/bin/python3


def no_c(my_string):
    str_copy = ""

    for character in my_string:
        if character.lower() != 'c':
            str_copy += character

    return str_copy
