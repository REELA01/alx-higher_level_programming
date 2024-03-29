#!/usr/bin/python3
"""defines student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initializtion """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj
            d_lis = {}
            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_lis[satr] = obj[satr]
            return d_lis
        return obj

    def reload_from_json(self, json):
        """replaces attributes"""
        for atr in json:
            self.__dict__[atr] = json[atr]
