#!/usr/bin/python3
def uppercase(str):
    for c in str:
        last = c
        if ord(c) >= 97 and ord(c) <= 122:
            last = chr(ord(c) - (ord('a') - ord('A')))
        print("{}".format(last), end="")
    print()
