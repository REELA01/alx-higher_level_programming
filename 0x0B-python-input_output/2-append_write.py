#!/usr/bin/python3
"""define a file-appending func"""


def append_write(filename="", text=""):
    """appends a string

    Args:
        filename: name of the file
        text: string txt
    Returns:
        The number of char
    """
    with open(filename, "a", encoding="utf-8") as file_3:
        return file_3.write(text)
