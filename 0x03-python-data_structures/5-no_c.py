#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for alphas in my_string:
        if alphas not in 'cC':
            new_str += alphas
    return new_str
