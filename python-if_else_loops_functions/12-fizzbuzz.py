#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        printer = i
        if i % 3 == 0 and i % 5 == 0:
            printer = "FizzBuzz"
        elif i % 3 == 0:
            printer = "Fizz"
        elif i % 5 == 0:
            printer = "Buzz"
        print("{} ".format(printer), end="")
