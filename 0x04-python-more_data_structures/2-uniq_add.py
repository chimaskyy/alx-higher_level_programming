#!/usr/bin/python3
def uniq_add(my_list=[]):

    """
    Fuction to add all unique element in a list

    set removes all duplicate element

    """
    if not my_list:
        return 0
    new = set(my_list)
    return sum(new)
