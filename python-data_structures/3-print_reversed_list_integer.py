#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    index = len(my_list)

    while index > 0:
        print("{:d}".format(my_list[index - 1]))
        index -= 1
