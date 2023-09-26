#!/usr/bin/python3
safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
