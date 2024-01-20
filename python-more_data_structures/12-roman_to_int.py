#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman = 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'I':
            roman += 1
        elif roman_string[i] == 'V':
            if i > 0 and roman_string[i - 1] == 'I':
                roman -= 2
            roman += 5
        elif roman_string[i] == 'X':
            if i > 0 and roman_string[i - 1] == 'I':
                roman -= 2
            roman += 10
        elif roman_string[i] == 'L':
            if i > 0 and roman_string[i - 1] == 'X':
                roman -= 20
            roman += 50
        elif roman_string[i] == 'C':
            if i > 0 and roman_string[i - 1] == 'X':
                roman -= 20
            roman += 100
        elif roman_string[i] == 'D':
            if i > 0 and roman_string[i - 1] == 'C':
                roman -= 200
            roman += 500
        elif roman_string[i] == 'M':
            if i > 0 and roman_string[i - 1] == 'C':
                roman -= 200
            roman += 1000
    return roman
