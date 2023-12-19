#!/usr/bin/python3
""" square class"""


class Square:
    """ square represntaion"""

    def __init__(self, size=0):
        """iinilization
        Args:
            size (int): square size
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
