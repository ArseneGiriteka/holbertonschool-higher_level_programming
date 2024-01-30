#!/usr/bin/python3


def roman_to_int(roman_string):
    result = 0
    i = 0
    _str = roman_string

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    while i < len(_str):
        symbol_1 = get_roman_value(_str[i])

        if i + 1 < len(_str):
            symbol_2 = get_roman_value(_str[i + 1])

            if symbol_2 <= symbol_1:
                result += symbol_1
                i += 1
            else:
                result += symbol_2 - symbol_1
                i += 2
        else:
            result += symbol_1
            i += 1
    return result


def get_roman_value(roman_string):
    if roman_string == 'D':
        return 500
    elif roman_string == 'M':
        return 1000
    elif roman_string == 'C':
        return 100
    elif roman_string == 'L':
        return 50
    elif roman_string == 'X':
        return 10
    elif roman_string == 'V':
        return 5
    elif roman_string == 'I':
        return 1
    else:
        return -1
