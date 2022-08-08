#!/usr/bin/python3
""" 4-print_square : prints a square with "#"
"""


def print_square(size):
    """prints a square with "#"
    Args:
        size (int) : length of the size of the square
    """
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            if (j == size - 1):
                print("#")
            else:
                print("#", end="")
