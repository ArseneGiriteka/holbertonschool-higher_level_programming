#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        i = 0

        for num in _list:
            print("{:d}".format(num), end="")
            if i != len(_list) - 1:
                print("", end=" ")
            i += 1
        print()
