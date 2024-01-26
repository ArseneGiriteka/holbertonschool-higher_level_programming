#!/usr/bin/python3
import sys


def main():
    num_args = len(sys.argv)
    print("{} argument".format(num_args - 1), end="")
    if num_args - 1 != 1:
        print("s", end="")
    if num_args - 1 == 0:
        print(".")
    else:
        print(":")
    for i in range(1, num_args):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
