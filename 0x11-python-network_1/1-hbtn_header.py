#!/usr/bin/python3

"""
Takes in a url, send a request to the URL and displays
 the value of the X-Request-Id variable found in the header
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

