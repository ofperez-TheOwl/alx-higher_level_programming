#!/usr/bin/python3
"""
Module 2-square
Defines class Square with private attribute size and validates size
"""


class Square:
    """Definition of class Square for Alx program
    """
    def __init__(self, size=0):
        """Initialization of Square object

        Args:
            size (int): Size of side of Square object
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
