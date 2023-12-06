#!/usr/bin/python3 
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    avg = 0
    base = 0
    for i in my_list:
        avg += i[0] * i[1]
        base += i[1]
    return avg / base
