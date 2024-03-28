#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as re:
        h = re.read()
        print("Body response:")
        print("\t- type: {}".format(type(h)))
        print("\t- content: {}".format(h))
        print("\t- utf8 content: {}".format(h.decode('utf-8')))
