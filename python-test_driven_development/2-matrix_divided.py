#!/usr/bin/python3
"""
This a new module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: The new matrix with elements divided by the divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
            or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
