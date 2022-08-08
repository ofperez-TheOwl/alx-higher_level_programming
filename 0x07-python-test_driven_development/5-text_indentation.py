#!/usr/bin/python3
""" 5-text_indentation : indents a text
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ".?:"
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")
    j = len(text)
    i = 0
    while (i < j):
        if (text[i] in [".", "?", ":"]):
            print(text[i], "\n", sep="")
            if (i + 1 < j and text[i + 1] == " "):
                while (text[i + 1] == " " and i + 1 < j):
                    i += 1
        else:
            print(text[i], end="")
        i += 1
