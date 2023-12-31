#!/usr/bin/python3
""" square class"""


class Square:
    """ repesentaion"""

    def __init__(self, size=0):
        """initialization
        Args:
            size (int): square size
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the area"""
        return self.__size**2
