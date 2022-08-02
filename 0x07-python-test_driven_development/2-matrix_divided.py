#!/usr/bin/python3
"""2-matrix_divided : divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix_divider : divides elements of matrix by div
    Arguments:
        matrix (list) : list of two list of number that have the same length
        div (int/float) : divisor of matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (type(matrix) is not list):
        raise TypeError(msg)
    if (len(matrix) < 2):
        raise TypeError(msg)
    if (type(matrix[0]) is list):
        n = len(matrix[0])
    for row in matrix:
        if (type(row) is not list):
            raise TypeError(msg)
        if (n != len(row)):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if (type(element) not in [int, float]):
                raise TypeError(msg)
    if (type(div) not in [int, float]):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
