#!/usr/bin/pyhton3
"""Module3-common_elements
"""


def common_elements(set_1, set_2):
    if (set_1 is not None and set_2 is not None):
        return (set_1 & set_2)
    return (None)
