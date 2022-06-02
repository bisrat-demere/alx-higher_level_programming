#!/usr/bin/python3
import sys

if __name__ == "__main__":

    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{}: arguments:".format(n-1))
        for y in range(1, len(sys.argv)):
            print("{}: {}".format(y, sys.argv[y]))
