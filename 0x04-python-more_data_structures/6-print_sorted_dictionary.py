#!/usr/bin/python3
"""Module : 6-print_sorted_dictionary
"""


def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary == dict):
        for i in sorted(list(a_dictionary)):
            print(i, ': ', a_dictionary[i], sep='')
