from urllib.request import Request
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re
import random
import json
import pandas as pd
import requests

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


# switch to next page
def nextPage(index):
    return f"https://careers.google.com/api/v3/search/?distance=50&hl=en&page={index}&q=software"


def crawler():
    job_dic = {}
    page = 0
    count = 0
    while True:
        count += 1
        page += 1
        url = nextPage(page)
        session = requests.Session()
        try:
            url_obj = session.get(url, headers=headers)
            bs = BeautifulSoup(url_obj.text, 'html.parser')
            job_dic[page] = bs.text
            print(page)
        except:
            print("Pages end.")
            break

        # Serializing json
        json_object = json.dumps(job_dic, indent=4)
        # Writing to sample.json
        with open(f"./raw_data/google_careers_page{page}.json", "w") as outfile:
            outfile.write(json_object)
        job_dic = {}
        time.sleep(random.randint(1, 20))


