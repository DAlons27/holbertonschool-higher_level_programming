def print_last_digit(number):
    ret = 0
    if number > 0:
        ret = number % 10
    elif number < 0:
        ret = (number * -1) % 10
    else:
        ret = 0
    print("{}".format(ret), end="")
    return ret
