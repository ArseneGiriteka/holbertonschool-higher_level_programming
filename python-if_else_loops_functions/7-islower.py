#!/usr/bin/python3
def islower(c):
    if isinstance(c, str) and len(c) == 1:
        if ord(c) >= 97 and ord(c) <= 122:
            return True

    return False
