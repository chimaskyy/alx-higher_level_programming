#!/usr/bin/python3

import sys
if __name__ == "__main__":

    arg = sys.argv[1:]
    count = len(arg)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(count))

    for i, val_args in enumerate(arg):
            print("{} : {}".format(i + 1, val_args))
