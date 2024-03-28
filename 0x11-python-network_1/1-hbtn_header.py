#!/usr/bin/python3
"""takes in a URL, sends a request to the URL display value of X-Request-Id"""
import urllib.request as re
import sys

if __name__ == "__main__":
    with re.urlopen(sys.argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
