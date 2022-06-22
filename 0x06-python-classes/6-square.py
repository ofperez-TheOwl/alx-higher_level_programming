#!/usr/bin/python3
"""
Module 5-square
Defines class Square with private size, position and public area
Can access and update size
Can print Square with '#' as unit
"""


class Square:
    """Definition of Square class for Alx program
    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the size of square

        Args:
            size (int): Size of Square object provide by user
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter of square size
        """
        return (self.__size)

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

    @property
    def position(self):
        """Getter of square position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter of square position

        Args:
            value (tuple): value of square postion provide by user
        """
        if type(value) != tuple or len(value) != 2 or \
                type(value[0]) != int or type(value[1]) != int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current area's square
            Return:
                area
        """
        return (self.__size**2)
    def my_print(self):
        """Prints Square image with '#'
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("\n" * self.__position[1], end="")
                print(self.__position[0] * " ", self.__size * "#",end='')
                print()
