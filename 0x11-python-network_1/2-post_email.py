#!/usr/bin/python3
"""Script that sends an email as param/ returns response body"""

import urllib
import urllib.request as re
import urllib.parse as pa
import sys

if __name__ == "__main__":
    rmail = {'email': sys.argv[2]}
    data = pa.urlencode(rmail)
    data = data.encode('utf-8')
    req = re.Request(sys.argv[1], data)
    with re.urlopen(req) as res:
        print(res.read().decode('utf-8'))
