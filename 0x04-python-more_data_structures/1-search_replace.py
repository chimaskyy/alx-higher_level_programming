#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Function to replace value in a list with another

    map applies lambda function to each element

    lambda checks if the current lement is equal to search
    and replace it with the new element

    returns modified list
    """

    if not my_list:
        return my_list
    new_list = list(map(lambda x: replace if x == search else x, my_list))

    return new_list
