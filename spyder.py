#!/usr/bin/env python
import requests
import re
import urlparse
import optparse
import argparse

def get_args():
    try:
        parser = optparse.OptionParser()
        parser.add_option("-t", "--target", dest="target_website", help="Target website example.com")
        value, options = parser.parse_args()
    except:
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", dest="target_website", help="Target website example.com")
        value = parser.parse_args()
    if not value.target_website:
        parser.error("[-] ERROR Missing argument, use --help or more info")
    else:
        return value

value = get_args()

target_URL = "http://" + value.target_website
found_links = []

def get_links(webpage):
    page = requests.get(webpage).content
    return re.findall('(?:href=")(.*?)"', page)
def seek_page(target_page):
    links = get_links(target_page)
    for url in links:
        url = urlparse.urljoin(target_page, url)
        if value.target_website.split(".")[0] in url and url not in found_links and "#" not in url:
            found_links.append(url)
            print("[+] " + url)
            seek_page(url)

print("[...] Starting crawler...\n")
try:
    seek_page(target_URL)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C, Stopping Crawler...")
    exit()
print("\n[+] Found all Possible links on target.")