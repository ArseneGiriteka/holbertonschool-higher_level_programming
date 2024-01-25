#!/usr/bin/python3
def islower(c):
    islower = False
    if isinstance(c, str):
        for d in c:
            if ord(d) >= 65 and ord(d) <= 90:
                islower = False
                break
            if ord(d) >= 97 and ord(d) <= 122:
                islower = True
    return islower
