#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    values = a_dictionary.values()
    max_number = max(values)
    for key, value in a_dictionary.items():
        if value == max_number:
            return key
