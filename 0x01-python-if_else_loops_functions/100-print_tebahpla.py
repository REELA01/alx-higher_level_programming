#!/usr/bin/python3
for i in range(25, -1, -1):
    ch = i + ord('A')
    if ch % 2 == 0:
        ch += 32
    print("{:c}".format(ch), end="")
