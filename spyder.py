#!/usr/bin/env python
import requests
import re

def seek(url):
    try:
        return requests.get("https://" + url)
    except:
        pass

target_website = "google.com"
page = seek(target_website).content
links = re.findall('(?:href=")(.*?)"', page)

print(links)
#test each link for response