#!/usr/bin/python3
"""define file insertion func"""


def append_after(filename="", search_string="", new_string=""):
    """insert txt after each line containing a given str"""

    txt = ""
    with open(filename) as file_1:
        for line in file_1:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as file_2:
        file_2.write(txt)
