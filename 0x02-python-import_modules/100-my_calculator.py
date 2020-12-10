#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = argv[2]
        if op != "+" and op != "-" and op != "*" and op != "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = argv[1]
            b = argv[3]
            val_a = int(a, 10)
            val_b = int(b, 10)
            if op == "+":
                res = add(val_a, val_b)
            elif op == "-":
                res = sub(val_a, val_b)
            elif op == "*":
                res = mul(val_a, val_b)
            else:
                res = div(val_a, val_b)
            print("{:d} {} {:d} = {:d}".format(val_a, op, val_b, res))
