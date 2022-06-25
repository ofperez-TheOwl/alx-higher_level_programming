#!/usr/bin/python3
"""Module 1-search_replace
"""


def search_replace(my_list, search, replace):
    return ([i if i != search else replace for i in my_list])
