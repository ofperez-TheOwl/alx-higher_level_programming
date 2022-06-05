#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return (None)
    if (len(my_list) == 1):
        return (my_list[0])
    i = my_list[0]
    for j in my_list:
        if (i < j):
            i = j
    return (i)
