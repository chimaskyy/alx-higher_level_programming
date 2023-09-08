#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    args = sys.argv
    ac = len(args)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operate = {
            "+": calc.add,
            "-": calc.sub,
            "*": calc.mul,
            "/": calc.div
            }

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if sys.argv[2] not in operate:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

        if op == "/" and b == 0:
            print("Division by 0 rejected")
            exit(1)

    print("{} {} {} = {}".format(a, op, b, operate[op](a, b)))
