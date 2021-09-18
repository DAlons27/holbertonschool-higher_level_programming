#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for m in matrix:
        new.append(list(map(lambda x: x*x, m)))
    return new
