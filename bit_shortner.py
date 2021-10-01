# Import the modules

import bitlyapi
import sys

# Define your API information

API_USER = "your_api_username"
API_KEY = "your_api_key"

b = bitlyapi.BitLy(API_USER, API_KEY)

# Define how to use the program

usage = """Usage: python shortener.py [url]
e.g python shortener.py http://www.google.com"""

if len(sys.argv) != 2:
    print usage
    sys.exit(0)

longurl = sys.argv[1]

response = b.shorten(longUrl=longurl)

print response['url']