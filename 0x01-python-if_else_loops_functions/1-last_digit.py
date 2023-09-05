#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = "-" + str(number)[-1]
else:
    digit = str(number)[-1]

if int(digit) > 5:
    print("Last digit of", number, "is", digit, "and is greater than 5")
elif int(digit) == 0:
    print("Last digit of", number, "is", digit, "and is 0")
elif int(digit) < 6 and int(digit) != 0:
    print("Last digit of", number, "is", digit, "and is less than 6 and not 0")
