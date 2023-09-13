#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    new_l = []
    for i in matrix:
        new_l.append(list(map(lambda n: n ** 2, i)))
    return new_l
