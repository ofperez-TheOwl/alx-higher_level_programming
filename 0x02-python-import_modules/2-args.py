#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    arg = sys.argv
    if (len(arg) == 1):
        print("0 arguments.")
    else:
        if (len(arg) == 2):
            print("1 argument:")
            print("1: {:s}".format(arg[1]))
        else:
            print("{:d} arguments:".format(len(arg) - 1))
            for i in range(1, len(arg)):
                print("{:d}: {:s}".format(i, arg[i]))
