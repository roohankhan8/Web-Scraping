from argparse import ONE_OR_MORE
# from asyncio.base_subprocess import Website
from pickletools import bytes4

# There are two ways to scrape a WriteSubprocessPipeProto
# 1. Using API
# 2. HTML scraping using bs4

# STEP ONE: Install requirements
# pip install requests, bs4, html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# STEP TWO: Parse HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# STEP THREE: HTML Tree Traversal
title = soup.title
# print(title)
# print(type(title))
# print(type(soup))
# print(type(title.string))

# GET ALL PARAGRAPHS
# print(soup.find_all('p'))
# print(soup.find('p'))
# print(soup.find('p')['class'])
# print(soup.find_all('p', class_= 'mt-2'))
# print(soup.find('p').get_text())

# GET ALL ANCHORS
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if (link.get('href') !='#'):
        # all_links.add('https://codewithharry.com' + link.get('href'))
        linkText = 'https://codewithharry.com' + link.get('href')
        all_links.add(link)
        # print(linkText)

# mainDiv = soup.find(id='__next')
# for elem in mainDiv.strings:
#     print(elem)
# for item in mainDiv.parents:
#     print(item.name)
# for kids in mainDiv.children:
#     print(kids.name)

