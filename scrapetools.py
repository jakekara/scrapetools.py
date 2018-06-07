# --------------------------
# scrapetools.py
#
# tools for downloading all links on a web page, such as a
# table of CSV files
#
# jakekara
# jake@jakekara.com
# January 2017
# --------------------------

import requests, os
from bs4 import BeautifulSoup

# For setting up directory structure to store scraped data
def makedir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Get data or throw an exception. 
def get(url):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("get(): Status Not OK");
    return r.content

# Get and save data (in binary mode in case of Excel or other formats)
def download_bin(url,output_file):
    outfh = open(output_file,"wb")
    outfh.write(get(url))
    outfh.close()
    
# Get all CSVs (or other files) linked
# match_term is case-insensitive, and should probably be used for file extensions
# base_url is a function to prepend a base_url, default does nothing
# fname is a function to return a relative path to the output filename
def get_files(html, base_url=lambda x: x, match_term=".xls", fname=lambda x: x):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.findAll("a")
    for link in links:
        if link["href"] == None:
            continue
        url = link["href"]
        if match_term.upper() in url.upper():
            # print fname(url)
            download_bin(base_url(url),fname(url))

