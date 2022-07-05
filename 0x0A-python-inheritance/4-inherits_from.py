#!/usr/bin/python3
"""Module:4-inherits_from
check if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """check if object obj is inherited from class a_class

    Args:
        obj (any) : python object to analyze
        a_class (any) : python class to analyze

    Return: boolean; True if obj is a_class; if not False
    """
    return (issubclass(type(obj), a_class) if type(obj) != a_class else False)
