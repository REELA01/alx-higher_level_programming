#!/usr/bin/python3
"""takes your GitHub credentials and uses the GitHub API"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    a = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=a)
    print(req.json().get("id"))
