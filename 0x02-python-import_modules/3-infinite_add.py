#!/usr/bin/python3
import sys

if __name__ == "__main__":

    n = len(sys.argv)
    sum = 0
    if n == 1:
        print(sum)
    else:
        for y in range(1, len(sys.argv)):
            sum += int(sys.argv[y])
        print(sum)
