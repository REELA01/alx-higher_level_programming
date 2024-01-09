#!/usr/bin/python3
"""define a JSON file-reading funct"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename) as file_5:
        return json.load(file_5)
