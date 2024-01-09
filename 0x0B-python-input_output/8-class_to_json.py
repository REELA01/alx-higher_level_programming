#!/usr/bin/python3
""" class_to_json function"""


def class_to_json(obj):
    """Return dect descripiton of obj """

    r = {}
    if hasattr(obj, "__dict__"):
        r = obj.__dict__.copy()
    return r
