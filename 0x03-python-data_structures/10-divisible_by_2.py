#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    l = []
    for i in my_list:
        if (i % 2) == 0:
            l.append(True)
        else:
            l.append(False)
    return l

