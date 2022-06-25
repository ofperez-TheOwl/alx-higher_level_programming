#!/usr/bin/python3
"""Module : 2-uniq_add
"""


def uniq_add(my_list=[]):
    result = 0
    for i in set(my_list):
        result = result + i
    return (result)
