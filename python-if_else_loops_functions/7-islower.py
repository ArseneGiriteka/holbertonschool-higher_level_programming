#!/usr/bin/python3
def islower(c):
    if isinstance(c, str):
        for d in c:
            if ord(d) >= 65 and ord(d) <= 90:
                return False

    return True
