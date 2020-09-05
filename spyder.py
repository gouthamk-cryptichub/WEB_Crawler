#!/usr/bin/env python
import requests
import re
import urlparse

target_website = "google.com"

target_URL = "http://" + target_website
foubd_links = []
def get_links(website):
    page = requests.get(target_URL).content
    return re.findall('(?:href=")(.*?)"', page)

links = get_links(target_website)
for url in links:
    url = urlparse.urljoin(target_URL, url)
    if target_website.split(".")[0] in url and url not in found_links and "#" not in url:
        foubd_links.append(url)
        print(url)
