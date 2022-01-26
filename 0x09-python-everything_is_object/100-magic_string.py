#!/usr/bin/python3
def magic_string(i=[0]):
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Best, " * (magic_string.n - 1) + "School")


