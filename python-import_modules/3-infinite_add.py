#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_arg = len(argv) - 1
    suma = 0
    for i in range(len_arg):
        suma += int(argv[i + 1])
    print("{}".format(suma))
