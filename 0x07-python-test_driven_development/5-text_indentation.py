#!/usr/bin/python3
"""
This module prints text
Prints 2 new line after . , : , and ?
"""

def text_indentation(text):
    """
    Function that prints text
    Prints 2 new line after chars . , ? and :
    Arg:
        text: Text to print
    """
    for chars in text:
        print(chars, end="")
        if chars in [".", ":", "?"]:
            print("\n\n", end="")
    if type(text) is not str:
        raise TypeError('text must be a string')
