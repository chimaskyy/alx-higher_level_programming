#!/usr/bin/python3
for num in range(10):
    for num2 in range(10):
        if num == num2 or num2 < num:
            continue
        if num != 8 or num2 != 9:
            print("{}{}".format(num, num2), end=", ")
        else:
            print("{}{}".format(num, num2), end="\n")
