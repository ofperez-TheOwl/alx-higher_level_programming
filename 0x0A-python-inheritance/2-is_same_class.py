#!/usr/bin/python3
"""Module:2-is_same_class
check if an object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """check if object obj is of class a_class

    Args:
        obj (any) : python object to analyze
        a_class (any) : python class to analyze

    Return: boolean; True if obj is a_class; if not False
    """
    return (type(obj) == a_class)
