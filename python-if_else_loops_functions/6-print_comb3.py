#!/usr/bin/python3
for c in range(0, 10):
    for d in range(c + 1, 10):
        if c != 8 or d != 9:
            print("{}{},".format(c, d), end=" ")
        else:
            print("{}{}".format(c, d))
