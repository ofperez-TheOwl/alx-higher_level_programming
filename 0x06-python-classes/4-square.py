#!/usr/bin/python3
"""
Module 4-square
Defines class Square with private size and public area
Can access and update size
"""


class Square:
    """Definition of Square class for Alx program
    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """
    def __init__(self, size=0):
        """Initialization of the size of square

        Args:
            size (int): Size of Square object provide by user
        """
        self.__size = size

    @property
    def size(self):
        """Getter of square size
        """
        return (self.size)

    @size.setter
    def size(self, value):
        """Setter of square size

        Args:
            value (int): value of square provide by user
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current area's square

        Returns:
            always area of square
        """
        return (self.__size**2)
