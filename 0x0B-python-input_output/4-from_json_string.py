#!/usr/bin/python3
"""define a JSON-to-str func"""
import json


def from_json_string(my_str):
    """Return str feom json represntaion"""
    return json.loads(my_str)
