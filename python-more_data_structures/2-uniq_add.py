#!/usr/bin/python3


def uniq_add(my_list=[]):
    s = 0

    for i in range(0, len(my_list)):
        if my_list[i] not in my_list[i + 1:]:
            s += my_list[i]
    return s
