#!/usr/bin/python3
"""Module : 9-multiply_by_2
"""


def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary:
        new_dict[i] = 2 * a_dictionary[i]
    return (new_dict)
