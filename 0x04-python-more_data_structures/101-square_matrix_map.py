#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda s: list(map(lambda e: e**2, s)), matrix))
