#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    i = None
    try:
        i = fct(args[0], args[1])
        return (i)
    except (IndexError, TypeError, ValueError, ZeroDivisionError, NameError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (i)
