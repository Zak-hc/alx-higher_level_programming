#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for element in x:
            print ("{}".format(element), end=" ")
        print('$')
