#!/usr/bin/python3


def weight_average(my_list=[]):
    res = 0
    w_sum = 0
    for item in my_list:
        res += item[0] * item[1]
        w_sum += item[1]
    return res / w_sum
