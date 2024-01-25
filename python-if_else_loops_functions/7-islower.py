#!/usr/bin/python3
def islower(c):
    is_lower = False
    if isinstance(c, str):
        for d in c:
            if ord(d) >= 65 and ord(d) <= 90:
                return False
            if ord(d) >= 97 and ord(d) <= 122:
                is_lower = True
    else:
        return False
    return is_lower
