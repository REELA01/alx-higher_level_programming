#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for k in range(0, x):
        try:
            print("{}".format(my_list[k]), end="")
            c += 1
        except (ValueError, TypeError, IndexError):
            break
    print()
    return c
