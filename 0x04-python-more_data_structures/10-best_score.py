#!/usr/bin/python3
"""Module : 10-best_score
"""


def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == { }:
        return (None)
    item = [a_dictionary[i] for i in sorted(a_dictionary)]
    item = sorted(item)
    for i in a_dictionary:
        if a_dictionary[i] == item[len(item) - 1]:
            break
    return (i)
