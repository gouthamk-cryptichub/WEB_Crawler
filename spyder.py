#!/usr/bin/env python
import requests
import re
import urlparse

target_website = "google.com"
target_URL = "http://" + target_website
organisation = target_website.split(".")[0]
def get_links(website):
    page = requests.get(target_URL).content
    return re.findall('(?:href=")(.*?)"', page)

links = get_links(target_website)
for url in links:
    url = urlparse.urljoin(target_URL, url)
    if organisation in url:
        print(url)
