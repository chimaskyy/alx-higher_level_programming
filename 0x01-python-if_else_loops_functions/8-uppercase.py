#!/usr/bin/python3
def uppercase(str):
    for chars in str:
        if ord(chars) >= 97 and ord(chars) <= 122:
            chars = chr(ord(chars) - 32)
        print("{}".format(chars), end='')
    print()
