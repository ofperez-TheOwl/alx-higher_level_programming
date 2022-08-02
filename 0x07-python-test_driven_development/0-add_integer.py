#!/usr/bin/python3
"""0-add_integer: adds two integer
"""


def add_integer(a, b=98):
    """adds two integer
    Arguments:
        a (int/float) : first number
        b (int/float) : second number
    """
    if (type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    if (type(b) not in [int, float]):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
