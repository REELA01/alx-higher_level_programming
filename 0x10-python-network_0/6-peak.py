#!/usr/bin/python3
"""finding the peak integer"""


def find_peak(list_of_integers):
    """Finds peak in ints"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
