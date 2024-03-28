#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request"""
import sys
import requests


if __name__ == "__main__":
    val = {"email": sys.argv[2]}

    req = requests.post(sys.argv[1], data=val)
    print(req.text)
