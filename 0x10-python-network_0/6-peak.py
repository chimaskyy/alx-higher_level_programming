#!/usr/bin/python3
"""This module finds a pead in list
unsorted integers
"""


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """
    # check if list is empty
    if not list_of_integers:
        return None

    # low starts at 0 high set to lat index of list
    low, high = 0, len(list_of_integers) - 1

    # perform binary search to find peak
    while low < high:
        # calculate middle inde
        mid = (low + high) // 2

    # check if peak is on the left of mid
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        # check right of mid
        else:
            low = mid + 1
    return list_of_integers[low]
