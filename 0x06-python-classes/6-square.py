#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and position but public area
Can access and update size
Can print Square with '#' as unit starting at position

TheOwl
"""


class Square:
    """Definition of Square class for Alx program
    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the size of square

        Args:
            size (int): Size of Square object provided by user
            position (tuple): coordinates of square object provided by user
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter of square size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter of square size

        Args:
            value (int): value of square provided by user
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
            value (tuple): coordinates of square provided by user
        """
        if (type(value) != tuple or len(value) != 2
                or type(value[0]) != int or type(value[1]) != int
                or value[0] < 0 or value[1] < 0):
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
            if self.position[1] > 0:
                print(self.__position[1] * "\n", end="")
            for i in range(self.__size):
                print(self.position[0] * ' ' + self.__size * "#")
