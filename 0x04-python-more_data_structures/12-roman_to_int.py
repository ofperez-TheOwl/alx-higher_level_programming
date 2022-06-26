#!/usr/bin/python3
"""Module : 12-roman_to_int
Can convert a roman numeral to an integer
"""


def roman_to_int(roman_string):
    uniq = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    substr = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    i, result = 0, 0
    if roman_string is None:
        return (0)
    if roman_string == "":
        return (0)
    while (i < len(roman_string)):
        if roman_string[i:i + 2] in substr:
            result = result + substr[roman_string[i:i + 2]]
            i = i + 2
        else:
            result = result + uniq[roman_string[i]]
            i = i + 1
    return (result)
