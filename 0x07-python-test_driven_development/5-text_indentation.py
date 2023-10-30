#!/usr/bin/python3
"""
    This module contains function that handles text indenting
"""


def text_indentation(text):
    """
       function that prints a text with 2 new lines after each
        of these chars: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    start = 0
    indenter = [".", "?", ":"]
    for chars in text:
        """check if string is whitespace"""
        if chars.isspace() and start == 0:
            continue
        elif chars in indenter:
            print("{}\n\n".format(chars), end="")
            start = 0
            continue
        else:
            print("{}".format(chars), end="")
            start += 1
