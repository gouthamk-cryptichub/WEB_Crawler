#!/usr/bin/env python
import requests

def seek(url):
    try:
        return requests.get("https://" + url)
    except:
        pass

target_website = "google.com"
with open ("subdomainlist.txt", "r") as wordlist:
    for word in wordlist:
        seek_url = word.strip() + "." + target_website
        resp = seek(seek_url)
        if resp:
            print("[+] Detected Subdomain --> " + seek_url)