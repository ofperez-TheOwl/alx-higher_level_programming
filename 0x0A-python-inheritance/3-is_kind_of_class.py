#!/usr/bin/python3
"""Module:3-is_kind_of_class
check if an object is an instance of a specified class
or a class inherited from that specified class
"""


def is_kind_of_class(obj, a_class):
    """check if object obj is kind of class a_class

    Args:
        obj (any) : python object to analyze
        a_class (any) : python class to analyze

    Return: boolean; True if obj is a_class; if not False
    """
    return (isinstance(obj, a_class))
