#!/usr/bin/env python
import requests

url = "fdgd.google.com"
try:
    get_resp = requests.get("https://" + url)
    print(get_resp)
except:
    print("url NOT FOUND")