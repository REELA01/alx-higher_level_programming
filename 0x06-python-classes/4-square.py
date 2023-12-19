#!/usr/bin/python3
""" sqaure class"""


class Square:
    """ reperesentaion"""
    def __init__(self, size=0):
         """initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """int: private size.
        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns area"""
        return self.__size**2
