#!/usr/bin/python3
def islower(c):
    is_lower = False
    for d in c:
        if 'A' <= d and d <= 'Z':
            return False
        elif ('a' <= d and 'z' >= d) or d == ' ':
            is_lower = True
    return is_lower
