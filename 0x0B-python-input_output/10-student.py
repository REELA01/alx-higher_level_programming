#!/usr/bin/python3
"""define class Student"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initializtion """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return directory description """
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
