#!/usr/bin/python3
"""defines file-reading func"""


def read_file(filename=""):
    """print UTF8 text  contetnt file to stdout"""
    with open(filename, encoding="utf-8") as file_1:
        print(file_1.read(), end="")
