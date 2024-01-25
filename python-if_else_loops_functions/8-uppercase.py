#!/usr/bin/python3


def uppercase(str):
    uppercase_chr = ''
    for c in str:
        if 97 <= ord(c) <= 122:
            uppercase_chr = chr(ord(c) - ord('a') + ord('A'))
        else:
            uppercase_chr = c
        print("{}".format(uppercase_chr), end="")
    print()
