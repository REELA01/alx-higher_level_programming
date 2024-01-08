#!/usr/bin/python3
"""define Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representing a rectangle"""

    def __init__(self, size):
        """intialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """computing area of square"""
        return self.__size ** 2

    def __str__(self):
        """official string representation"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
