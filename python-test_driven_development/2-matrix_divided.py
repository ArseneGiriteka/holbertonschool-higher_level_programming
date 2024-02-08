#!/usr/bin/python3
"""

This is the new module

"""


def matrix_divided(matrix, div):
    """
    This the new funcction
    """
    length = 0
    size_err = "Each row of the matrix must have the same size"
    other_err_1 = "matrix must be a matrix"
    other_err_2 = " (list of lists) of integers/floats"
    other_err = other_err_1 + other_err_2

    if not isinstance(matrix, list):
        raise TypeError(other_err)

    for _list in matrix:
        if not isinstance(_list, list):
            raise TypeError(other_err)
        for i in range(len(_list)):
            if not isinstance(_list[i], (int, float)):
                raise TypeError(other_err)

    length = len(matrix[0])
    for _list in matrix:
        if length != len(_list):
            raise TypeError(size_err)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(
        map(
            lambda _list: list(
                map(lambda x: round(x / div, 2), _list)), matrix))

    return new_matrix
