#!/usr/bin/python3
'''
This module contains a single function
'''


def pascal_triangle(n):
    '''
    print pascal's triangle
    '''
    if n <= 0:
        return []

    '''creat a triangle of ones in n rows from index 1'''
    triangle = [[1] * i for i in range(1, n + 1)]

    '''iterate throug each row of the triangle'''
    for i, row in enumerate(triangle):
        '''skip the first two rows of the triangle(already correctly set)'''
        if i < 2:
            continue

        '''iterate through each element in row
        skipping first and last element'''
        for j in range(1, len(row) - 1):
            '''sum of element above and to the left[i-1][j-1]
            and the element directly above[i-1][j]'''
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle
