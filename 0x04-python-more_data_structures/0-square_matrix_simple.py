#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        square = [x ** 2 for x in row]
        new_matrix.append(square)
    return (new_matrix)
