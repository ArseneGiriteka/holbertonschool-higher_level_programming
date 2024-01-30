#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return list(map(
        lambda _line: list(map(lambda x: x**2, (x for x in _line))),
        (_line for _line in matrix))
        )
