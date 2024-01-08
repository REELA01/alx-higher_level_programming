#!/usr/bin/python3
"""defines add_attribute func"""


def add_attribute(obj, atribute, val):
    """add a new attribute if passible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj,  atribute, val)
