#!/usr/bin/python3
"""Module : 2-rectangle
Defines a class Rectangle with width and height as private instance attriubutes
Initiates instance attributes
Computes perimeter and area of rectangle
"""


class Rectangle():
    """Definition of class Rectangle

    Args:
        width (int): size of the horizontal side of Rectangle
        height (int): size of the vertical side of Rectangle
    Functions:
        __init__(self, width, height)
        height(self)
        height(self, value)
        width(self)
        witdth.(self, value)
        area(self)
        perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """Initiates attributes
        Attributes:
            width (int): size of the horizontal side of Rectangle
            height (int): size of the vertical side of Rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """width getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width  to provided value
        Args:
            value (int) : size of rectangle's width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer\n")
        if value < 0:
            raise ValueError("width must be >= 0\n")
        self.__width = value

    @property
    def height(self):
        """height getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height to provided value
        Args:
            value (int) : size of rectangle height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer\n")
        if value < 0:
            raise ValueError("height must be >= 0\n")
        self.__height = value

    def area(self):
        """Compute and return area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """Compute and return perimeter of rectangle
        """
        return ((2 * (self.__height + self.__width))
                if (self.__height != 0 and self.__width != 0) else 0)
