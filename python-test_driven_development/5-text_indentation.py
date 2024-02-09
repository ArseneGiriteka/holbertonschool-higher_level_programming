#!/usr/bin/python3
"""
brand new module
"""


def text_indentation(text):
    """
    This is a function
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for ch in text:
        result += ch
        if ch in ('?', '.', ':'):
            result += '\n\n'
    results = result.split('\n')

    for i in range(len(results)):
        if i != (len(results) - 1):
            print(results[i].strip())
        else:
            print(results[i].strip(), end="")
