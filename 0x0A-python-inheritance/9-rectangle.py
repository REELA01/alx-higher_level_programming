#!/usr/bin/python3
"""defines Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representing a rectangle"""

    def __init__(self, width, height):
        """intialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """compute area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """official string representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
