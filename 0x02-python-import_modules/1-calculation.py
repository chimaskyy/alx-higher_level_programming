#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    print(dir(calc))
    a = 10
    b = 5
    result = calc.add(a, b)
    print("{} + {} = {}".format(a, b, result))
    result2 = calc.sub(a, b)
    print("{} - {} = {}".format(a, b, result2))
    result3 = calc.mul(a, b)
    print("{} * {} = {}".format(a, b, result3))
    result4 = calc.div(a, b)
    print("{} / {} = {}".format(a, b, result4))
