#!/usr/bin/python3

import sys

if __name__ == "__main__":

    args = sys.argv[1:]
    sum = 0

    for nums in args:
        sum += int(nums)
    
    print(sum)
