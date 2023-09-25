#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for nums in range(x):
            print(my_list[nums], end='')
            count += 1
        print()
    except IndexError:
        print()
        return count
    else:
        return count
