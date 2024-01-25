#!/usr/bin/python3
for c in range(0, 100):
    if c != 99:
        print("{}{},".format(c // 10, c % 10), end=" ")
    else:
        print("{}{}".format(c // 10, c % 10))
