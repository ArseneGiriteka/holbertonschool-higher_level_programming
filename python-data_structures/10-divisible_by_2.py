#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    _list = []

    for item in my_list:
        if item % 2 == 0:
            _list += [True]
        else:
            _list += [False]

    return _list
