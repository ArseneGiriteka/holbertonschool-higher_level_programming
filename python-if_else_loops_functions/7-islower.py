#!/usr/bin/python3
def islower(c):
    is_lower = False
    if len(c) > 1:
        return False
    for d in c:
        if 'A' <= d and d <= 'Z':
            return False
        elif 'a' <= d and 'z' >= d:
            is_lower = True
    return is_lower
