#!/usr/bin/python3

for alpha in range(97, 122):
    if alpha == 101 or alpha == 113:
        continue
    else:
        print("{}".format(chr(alpha)), end="")
