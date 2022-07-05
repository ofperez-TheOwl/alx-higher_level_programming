#!/usr/bin/python3
"""Module: 7-base_geometry
Empty class BaseGeometry
Can validate if a value is integer
"""


class BaseGeometry():
    """Definition of class BaseGeometry

    Functions:
        /* public instance methods */
        area (self)
        integer_validator(self, name, value):
    """

    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value > 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
