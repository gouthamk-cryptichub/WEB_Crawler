#!/usr/bin/env python
import requests

url = "google.com"
get_resp = requests.get("https://" + url)
print(get_resp)