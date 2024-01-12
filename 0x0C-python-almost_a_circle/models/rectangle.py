#!/usr/bin/python3
"""defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initalization"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """the width getter and setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """the height getter and setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x coordinate getter and setter"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y coordinate getter and setter"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area"""
        return self.width * self.height

    def display(self):
        """displays the rectangle"""
        rect = self.y * "\n"
        for i in range(self.height):
            rect += (" " * self.x)
            rect += ("#" * self.width) + "\n"
        print(rect, end='')

    def __str__(self):
        """returns string of rectangle info"""
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)
