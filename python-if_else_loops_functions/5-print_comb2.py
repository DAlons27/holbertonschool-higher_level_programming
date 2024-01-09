#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print("{:02.0f}, ".format(i), end="")
        continue
    print("{}".format(i))
