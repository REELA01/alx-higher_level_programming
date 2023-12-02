#!/usr/bin/pyhton3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    cob = my_list.copy()
    cob[idx] = element
    return cob
