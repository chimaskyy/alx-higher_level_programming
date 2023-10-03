#!/usr/bin/python3
"""
This module contains function that divides all elements of a matrix
The divisor must not be Zero
"""
def matrix_divided(matrix, div):
    """Function that divides elements of a matrix by a number
    The number must not be Zero and must be an integer or float
    Args:
        matrix: list of list
        div: the divisor
    Return: Returns a new matrix
    """

    if not matrix:
        return
    if type(matrix) is not list or\
        any(type(num) is not list for num in matrix):
        raise TypeError('matrix must be a matrix' 
                        + '(list of lists) of integers/floats')
    for row in matrix:
        for num in row:
            if type(num) not in (int,float):
                raise TypeError('matrix must be a matrix' 
                                + '(list of lists) of integers/floats')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(num / div, 2) for num in row] for row in matrix]



