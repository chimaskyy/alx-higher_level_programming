#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print(f"{num:02d}", end="\n")
    else:
        print(f"{num:02d}", end=", ")
