#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    max_item = len(my_list)
    new_list = sorted(my_list)
    for item in range(max_item):
        if item + 1 < max_item:
            if new_list[item] == new_list[item + 1]:
                continue
            sum += new_list[item]
    sum += new_list[max_item - 1]
    return sum
