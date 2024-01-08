#!/usr/bin/python3
"""Mylist class"""


class MyList(list):
    """the baseclass"""

    def print_sorted(self):
        """print in sorted ascending order"""
        print(sorted(self))
