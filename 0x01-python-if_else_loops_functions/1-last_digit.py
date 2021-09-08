#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number1 = number * -1
    a = number1 % 10 * -1
else:
    number1 = number
    a = number1 % 10
if a > 5:
    b = "and is greater than 5"
elif a == 0:
    b = "and is 0"
else:
    b = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, a, b))
