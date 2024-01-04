#!/usr/bin/python3
"""rectangke class"""


class Rectangle:
    """define rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiation"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        
    @property
    def width(self):
        """get width of rect"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get rect height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rect"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of rect"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Return rect with # char"""
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """Return official rep pf rect"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print massage on delete"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
