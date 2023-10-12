#!/usr/bin/python3
'''
This module contains a single function
'''

def append_after(filename="", search_string="", new_string=""):
    '''
    This function inserts a line of text to a file
    after another line'''
    
    with open(filename, 'r', encoding="utf-8")as f:
        data = f.readlines()

    with open(filename, 'w') as f:
        for line in data:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')


