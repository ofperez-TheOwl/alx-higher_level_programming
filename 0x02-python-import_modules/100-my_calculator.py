#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    from calculator_1 import add, sub, mul, div
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        i = 1
    else:
        arg = sys.argv
        a, b = int(arg[1]), int(arg[3])
        if (arg[2] == '+'):
            print("{:d} + {:d} = {}".format(a, b, add(a, b)))
            i = 0
        elif (arg[2] == '-'):
            print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
            i = 0
        elif (arg[2] == '*'):
            print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
            i = 0
        elif (arg[2] == '/'):
            print("{:d} / {:d} = {}".format(a, b, div(a, b)))
            i = 0
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            i = 1
    exit(i)
