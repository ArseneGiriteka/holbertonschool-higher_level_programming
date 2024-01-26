#!/usr/bin/python3

for index in range(0, ord('z') - ord('a') + 1):
    if index % 2 == 0:
        print("{}".format(chr(ord('z') - index)), end="")
    else:
        print("{}".format(chr(ord('Z') - index)), end="")
