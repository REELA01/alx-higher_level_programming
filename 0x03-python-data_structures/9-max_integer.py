#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    cp = my_list.copy()
    cp.sort()
    return cp[-1]
