#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mt = matrix.copy()
    for i in range(len(matrix)):
        mt[i] = list(map(lambda x: x ** 2, matrix[i]))
    return mt
