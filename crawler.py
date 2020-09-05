#!/usr/bin/env python
import requests
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

def seek(url):
    try:
        return requests.get("https://" + url)
    except:
        pass

def run(target_website):
    with open ("subdomainlist.txt", "r") as wordlist:
        for word in wordlist:
            seek_url = word.strip() + "." + target_website
            resp = seek(seek_url)
            if resp:
                print("[+] Detected Subdomain --> " + seek_url)
                with open("directory.txt", "r") as word_list:
                    for wrd in word_list:
                        seek_dir = seek_url + "/" + wrd.strip()
                        resp_dir = seek(seek_dir)
                        if resp_dir:
                            print("\t[+] Found Page --> " + seek_dir)


value = get_args()
print("[...] Starting crawler...\n")
try:
    run(value.target_website)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C, Stopping Crawler...")
    exit()
print("\n[+] Found all Possible links on target.")
