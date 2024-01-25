#!/usr/bin/python3

def islower(c):
    is_lower = False

    for d in c:
        if 'A' <= d <= 'Z':
            return False
        elif 'a' <= d <= 'z':
            is_lower = True

    return is_lower
