#!/usr/bin/python3


def best_score(a_dictionary):
    max_score = 0
    max_key = ''
    if a_dictionary is None:
        return None
    for item in a_dictionary.items():
        if item[1] > max_score:
            max_score = item[1]
            max_key = item[0]
    return max_key


"""
short code

def best_score = lambda a_dictionary: max(map(
lambda item: item[0] if item[1] == max(a_dictionary.values()) else '',
a_dictionary.items())) if a_dictionary else None
"""
