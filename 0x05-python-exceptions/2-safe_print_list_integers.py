#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            c += 1
        except (ValueError, TypeError):
            continue
    print()
    return c
