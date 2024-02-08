#!/usr/bin/python3
"""

This is the new module

"""


def matrix_divided(matrix, div):
    """
    This the new funcction
    """
    length = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for _list in matrix:
        length = len(matrix[0])
        if not isinstance(_list, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif length != len(_list):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for i in _list:
                if not isinstance(i, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(
        map(
            lambda _list: list(
                map(lambda x: round(x / div, 2), _list))
            ,matrix))

    return new_matrix