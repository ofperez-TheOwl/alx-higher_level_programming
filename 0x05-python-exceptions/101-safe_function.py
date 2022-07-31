#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    i = None
    try:
        if (len(args) > 0):
            i = fct(*args)
        else:
            fct()
        return (i)
    except (IndexError, TypeError, ValueError, ZeroDivisionError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (i)
