#!/usr/bin/python3

"""
z = x + y

=>
(z1, z2) = (x1, x2) + (y1, y2)
=>
(z1, z2) = (x1 + y1, x2 + y2)
=>
z1 = x1 + y1
z2 = x2 + y2
"""


def add_tuple(tuple_a=(), tuple_b=()):
    x1, x2, y1, y2 = 0, 0, 0, 0

    if len(tuple_a) > 0:
        x1 = tuple_a[0]
    if len(tuple_a) > 1:
        x2 = tuple_a[1]
    if len(tuple_b) > 0:
        y1 = tuple_b[0]
    if len(tuple_b) > 1:
        y2 = tuple_b[1]

    return tuple((x1 + y1, x2 + y2))
