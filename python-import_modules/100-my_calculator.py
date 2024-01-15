#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        op = ["+", "-", "*", "/"]
        f = [
            calculator_1.add, calculator_1.sub,
            calculator_1.mul, calculator_1.div
                ]
        if not(sys.argv[2] in op):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            c = -1
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            for i in range(4):
                if sys.argv[2] == op[i]:
                    c = i
            print("{:d} {:s} {:d} = {:d}".format(a, op[c], b, f[c](a, b)))
