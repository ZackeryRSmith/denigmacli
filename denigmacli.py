#!/bin/python3
import requests
import sys
import json
import cloudscraper

def parse_code_file(path):
    form_dict = {}
    with open(path) as file:
        for line in file.readlines():
            form_dict[line] = ""
    return form_dict

form_data = parse_code_file(sys.argv[1])

scraper = cloudscraper.create_scraper(
    browser={
        "browser" : "chrome",
        "platform" : "windows",
        "desktop" : True
    }
)

req = scraper.request(
    "POST",
    "https://service.denigma.app/explain/demo/?p=1&engine_version=1",
    data=form_data
)

for line in json.loads(req.text)["data"]:
    print(line)