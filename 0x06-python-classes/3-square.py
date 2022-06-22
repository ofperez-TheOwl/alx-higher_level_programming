#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size and public attribute area
"""


class Square:
    """Definition of class Square object

    Args:
        size (int): size of a side in square
    Functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """Initialization of the size of side of square

        Args:
            size (int): Size of Square object
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current area's square

        Returns:
            always self.__size
        """
        return (self.__size**2)
