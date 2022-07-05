#!/usr/bin/python3
"""Module: 1-my_list
Defines class MyList inherited from list
can print content in ascending order
"""


class MyList(list):
    """Definition of MyList
    Inherites all the methods of the class list

    Functions:
        #public instance method
        print_sorted(self)
    """

    def print_sorted(self):
        """prints the list of int in ascending order"""
        print(sorted(self))
