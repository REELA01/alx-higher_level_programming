#!/usr/bin/python3
"""define a JSON file-writing func"""
import json


def save_to_json_file(my_obj, filename):
    """write to file using JSON representation."""
    with open(filename, "w") as file_4:
        json.dump(my_obj, file_4)
