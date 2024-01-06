#!/usr/bin/python3
"""say_my_name function"""


def say_my_name(first_name, last_name=""):
    """to orint first and last name

    Args:
        first_name: the strinf of first name
        last_name: string of the last name

    Raises:
        TypeError: if name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
