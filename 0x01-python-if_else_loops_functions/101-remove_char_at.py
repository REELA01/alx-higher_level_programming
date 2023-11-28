#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for m, c in enumerate(str):
        if m != n:
            s += c
    return s
