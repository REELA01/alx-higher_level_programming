#!/usr/bin/python3
"""define a file-writing func"""


def write_file(filename="", text=""):
    """write a string

    Args:
        filename: name of file
        text: txt of file
    Returns:
        The number of char
    """
    with open(filename, "w", encoding="utf-8") as file_2:
        return file_2.write(text)
