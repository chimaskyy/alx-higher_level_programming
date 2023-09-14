#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    convert roman numeral to integer
    roman_string - roman string to be converted
    rom - map ROman numeral to to corresponding int val
    check for empty input
    result stores accumulated int val
    iterate through each chars inroman_string
    check for end of string
    compare val of current char with the next,
    if current is less, substraction is carried out
    otherwise add val of current char to result
    """
    rom = {"I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000
           }

    if not roman_string:
        return 0
    if not rom:
        return 0
    result = 0

    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string)) and (rom[roman_string[i]] <
                                            rom[roman_string[i + 1]]):
            result -= rom[roman_string[i]]
        else:
            result += rom[roman_string[i]]
    return result
