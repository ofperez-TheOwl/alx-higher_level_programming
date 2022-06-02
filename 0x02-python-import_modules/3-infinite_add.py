#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    if (len(sys.argv) == 1):
        print(f"{0:d}")
    else:
        arg = sys.argv
        result = 0
        for i in range(1, len(arg)):
            result = result + int(arg[i])
        print(f"{result:d}")
