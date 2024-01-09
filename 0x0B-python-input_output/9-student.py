#!/usr/bin/python3
"""define the class Student"""


class Student:
    """create student instanse """

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns directory description """
        return self.__dict__.copy()
