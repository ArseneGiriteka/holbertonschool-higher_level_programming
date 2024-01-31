#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    res = 0
    i = 0

    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
            res_list += [res]
        except ZeroDivisionError:
            print("division by 0")
            res_list += [0]
        except TypeError:
            print("wrong type")
            res_list += [0]
        except IndexError:
            print("out of range")
            res_list += [0]
        finally:
            i += 1
    return res_list
