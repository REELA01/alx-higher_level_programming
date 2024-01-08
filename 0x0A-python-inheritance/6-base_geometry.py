#!/usr/bin/python3
"""define BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """define area with exeption"""
        raise Exception('area() is not implemented')
