#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list
    for x in range(len(a), 0, -1):
        print("{}".format(x))
