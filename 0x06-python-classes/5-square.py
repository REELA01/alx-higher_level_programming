#!/usr/bin/python3
""" class square"""


class Square:
    """ repeersentaion"""
    def __init__(self, size=0):
        """ initiliziation new sq

        Args:
            value (int): sq size
        """
        self.size = size

    @property
    def size(self):
        """int: private size

        Return:
            private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set ne value

        Args:
            value (int): sq size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the area

        Return:
            area
        """
        return self.__size**2

    def my_print(self):
        """print # sq"""

        if self.__size != 0:
            for k in range(self.__size):
                for b in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
