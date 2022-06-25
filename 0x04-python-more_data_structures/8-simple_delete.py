#!/usr/bin/python3
"""Module : 8-simple_delete
"""


def simple_delete(a_dictionary, key=""):
    if (key in a_dictionary):
        del a_dictionary[key]
    return (a_dictionary)
