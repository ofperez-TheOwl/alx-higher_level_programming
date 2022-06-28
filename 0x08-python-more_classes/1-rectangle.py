#!/usr/bin/python3
"""Module : 1-rectangle
Defines a class Rectangle with width and height as private instance attriubutes
It can initiate instance attributes
"""


class Rectangle():
    """Definition of class Rectangle object

    Args:
        width (int): size of the smaller side of Rectangle
        height (int): size of the greater side of Rectangle
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """

    def __init__(self, width=0, height=0):
        """Initialization of height and width
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width of rectangle to provided value
            Args:
                value (int) : new value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer\n")
        if value < 0:
            raise ValueError("width must be >= 0\n")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height of rectangle to provided value
            Args:
                value (int) : new value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer\n")
        if value < 0:
            raise ValueError("height must be >= 0\n")
        self.__height = value
