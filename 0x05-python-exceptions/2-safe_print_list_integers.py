#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if x == 0:
        print()
        return 0
    count = 0
    for num in range(x):
        try:
            print("{:d}".format(num), end="")
            count += 1
        except IndexError:
            raise
        except Exception:
            pass
    print()
    return count
