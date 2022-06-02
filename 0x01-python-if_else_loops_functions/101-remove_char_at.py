#!/usr/bin/python3
def remove_char_at(str, n):
    str = str[:n + 1] + str[n + 2:]
