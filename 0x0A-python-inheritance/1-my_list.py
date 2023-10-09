#!/usr/bin/python3
"""
This  module contains a single function
Prints a list in sorted form
"""


class MyList(list):

    """
    Defined class
    """

    def __init__(self, *args):
        """
        instance initialization
        """
        super.__init__(*args)

    def print_sorted(self):
        """
        Function that print list in ascending order
        """

    new_list = sorted(self)
    print(new_list)
