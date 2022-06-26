#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is None):
        return (None)
    if (value not in a_dictionary.values()):
        return (a_dictionary.copy())
    new_dict = a_dictionary.copy()
    for i in new_dict:
        if (new_dict[i] == value):
            del a_dictionary[i]
    new_dict = a_dictionary.copy()
    return (new_dict)
