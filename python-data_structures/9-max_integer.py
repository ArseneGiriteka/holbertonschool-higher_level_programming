#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None

    max_num = my_list[0]

    for item in my_list[1:]:
        if max_num < item:
            max_num = item

    return max_num
