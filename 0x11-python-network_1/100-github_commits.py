#!/usr/bin/python3
""" script that takes 2 arguments in order to solve this challenge"""
import sys
import requests


if __name__ == "__main__":

    req = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]))
    comm = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                comm[i].get("sha"),
                comm[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
