#!/usr/bin/env python
import requests
import re
import urlparse

target_website = "altoromutual.com"

target_URL = "http://" + target_website
found_links = []

def get_links(webpage):
    page = requests.get(webpage).content
    return re.findall('(?:href=")(.*?)"', page)

def seek_page(target_page):
    links = get_links(target_page)
    for url in links:
        url = urlparse.urljoin(target_page, url)
        if target_website.split(".")[0] in url and url not in found_links and "#" not in url:
            found_links.append(url)
            print("[+] " + url)
            seek_page(url)

print("[...] Starting crawler...\n")
seek_page(target_URL)
print("\n[+] Found all Possible links on target.")