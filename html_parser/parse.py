#!/usr/bin/python3
"""
a module to parse an extracted shegergebeta html page
"""
import requests
from bs4 import BeautifulSoup

with open("messages2.html") as f:
    parsed_url = f.read()
# html_text = requests.get(parsed_url).text

soup = BeautifulSoup(parsed_url, 'html.parser')

# for link in soup.find_all('div', {'class':'message service'}):
#     print(f'review date = {link.text.strip()}')

for links in soup.find_all('div', {'class':'message default clearfix'}):
    print(links.text)