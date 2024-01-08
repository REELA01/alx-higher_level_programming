#!/usr/bin/python3
"""define inherits_from"""


def inherits_from(obj, a_class):
    """if true subclass of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
