#!/usr/bin/python3
""" 3-say_my_name : prints My name <first name> <last name>
"""

def say_my_name(first_name, last_name=""):
    """prints name
    Arguments:
        first_name (string) : first name
        last_name (string) : last name
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
