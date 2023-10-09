#!/usr/bin/python3
"""
This  module contains a single function
Prints a list in sorted form
"""


class MyList(list):

    """
    Defined class
    """

    def print_sorted(self):
        """
        Function that print list in ascending order
        """
        new_list = sorted(self)
        print(new_list)
