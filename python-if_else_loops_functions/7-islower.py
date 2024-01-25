#!/usr/bin/python3

def islower(c):
    is_lower = False

    for d in c:
        if 'a' <= d <= 'z':
            is_lower = True
        elif 'A' <= d <= 'Z':
            return False
        else:
            continue

    return is_lower
