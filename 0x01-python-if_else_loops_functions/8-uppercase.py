#!/usr/bin/python3
def uppercase(str):
    for c in str:
        last = c
        if ord(c) >= ord('a') and ord(c) <= ('z'):
            last = chr(ord(c) - (ord('a') - ord('A')))
        print("{}".format(last), end="")
    print()
