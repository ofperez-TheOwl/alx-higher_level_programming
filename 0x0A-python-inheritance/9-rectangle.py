#!/usr/bin/python3
"""Module: 8-rectangle
Defines a Rectancle class with
width and height as private instance attributes
can calculate area of rectangle
have a string pattern
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of Rectangle class

    Args:
        /* private instance attributes */
        width (int)
        height (int)

    Functions:
        /* magic methods */
        __init__(self, width, height)
        __str__(self)
        /* public instance methods */
        area(self)
    """

    def __init__(self, width, height):
        """initialize width and height of new rectangle
        Attributes:
            width (int) : size of the width of rectangle
            height (int) : size of the height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area of the rectangle
            Return: int; area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """provide pattern for printing rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
