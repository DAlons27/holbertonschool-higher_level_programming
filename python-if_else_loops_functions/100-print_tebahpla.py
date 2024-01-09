#!/usr/bin/python3
for i in range(-90, -64):
    num = i * -1
    if num % 2 == 0:
        print("{}".format(chr(num + 32)), end="")
    else:
        print("{}".format(chr(num)), end="")
